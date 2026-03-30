import pytest
from app import app
from tools import Tool

@pytest.fixture
def client():
    """
    Zet Flask-app in testmodus en maakt een testclient aan.
    Hiermee kunnen we requests naar de server sturen zonder de app te draaien.
    """
    app.config['TESTING'] = True  # Activeer de testomgeving binnen Flask
    return app.test_client()


# 1. Werkt de website?
def test_website(client):
    """
    Controleert of de website werkt
    """
    response = client.get('/')      # Voer een GET-request uit op de root-URL
    assert response.status_code == 200  # Controleer of de server HTTP 200 (OK) teruggeeft


# 2. DYNAMISCHE PAGINA: (Happy Flow)
def test_DYNAMISCHE_valid(client):
    """
    Test of het formulier correct wordt verwerkt zonder de pijplijn te starten.
    """
    payload = {                               
        "fastq_bestand": "data.fastq",
        "nucleotiden_achter_elkaar": "10",
        "afstand_matches": "5",
        "maximaal_keer_gerapporteerd": "2"
    }
    response = client.post('/bmf', data=payload)  # Verstuur de data via een POST-request naar /bmf
    assert response.status_code == 200            # Controleer of de pagina succesvol reageert


# 3. UNIT TEST: Test de __str__ methode 
def test_tool_str_output():
    """
    Test of de Tool-klasse een correcte leesbare string geeft.
    """
    test_tool = Tool(                 # Maak een nieuw Tool-object aan met specifieke variabelen
        method="test_method", 
        input_file="input.fq", 
        output_file="output.vcf",
        refseq="ref.fna",
        tweaks="-x"
    )
    output_str = str(test_tool)       # Roep de __str__ methode 
    assert "method: test_method" in output_str  # Check of de methode-naam in de string staat
    assert "input file: input.fq" in output_str  # Check of de inputfile in de string staat
    assert "refseq: ref.fna" in output_str       # Check of de referentie-sequentie in de string staat
    assert "tweaks: -x" in output_str            # Check of de extra parameters in de string staan


# 4. test bwa_mem commando's
def test_bwa_mem2_arguments():
    """
    Test of de bwa_mem2 commando's (k, w en c parameters) correct worden opgebouwd.
    """
    test_k, test_w, test_c = "15", "10", "5"  # Definieer test-waarden voor de argumenten
    bwamem2 = Tool(                           # Maak een Tool-object specifiek voor bwa-mem2
        method=f"bwa-mem2 mem -k {test_k} -w {test_w} -c {test_c}",
        refseq="referentie/ref.fna",
        input_file="data.fastq",
        output_file="output/output.sam"
    )
    args = bwamem2.arguments()                
    assert f"-k {test_k}" in args             
    assert f"-w {test_w}" in args 
    assert f"-c {test_c}" in args          
    assert "bwa-mem2 mem" in args            
    assert "-o output/output.sam" in args     


# 5. Test de view functie in samtools
def test_samtools_view_arguments():
    """
    Test de 'view' methode van de samtools in tools.py.
    """
    test_tool = Tool(                 
        method="samtools view",
        input_file="input.sam",
        output_file="output.bam",
        tweaks="-b"
    )
    args = test_tool.arguments()   
    assert "samtools view" in args    
    assert "-b" in args              
    assert "-o output.bam" in args 


# 6. TEST bcftools mpileup 
def test_bcftools_mpileup_arguments():
    """
    Test de mpileup van de bcftools in tools.py
    """
    bcftools_mpileup = Tool(       
        method="bcftools mpileup",
        refseq="referentie/genome.fna",
        input_file="output/sorted.bam",
        output_file="output/mpileup.bcf"
    )
    args = bcftools_mpileup.arguments()      
    assert "bcftools mpileup" in args         
    assert "-f referentie/genome.fna" in args 
    assert "-o output/mpileup.bcf" in args   
    assert "output/sorted.bam" in args    


# 7. EDGE CASE: Verkeerd bestandstype 
def test_invalid_bestanden(client):
    """
    Test hoe de website reageert op een ongeldige bestandsextensie (.pdf).
    """
    payload = {                               # Maak een payload met een foutieve extensie
        "fastq_bestand": "document.pdf",      # PDF is niet toegestaan voor bio-informatica tools
        "nucleotiden_achter_elkaar": "10",
        "afstand_matches": "5",
        "maximaal_keer_gerapporteerd": "2"
    }
    response = client.post('/bmf', data=payload)  # Verstuur de foutieve data
    # Controleer of de pagina herlaadt maar GEEN succesmelding ('STATUS') toont
    assert b"STATUS" not in response.data    


# 8. EDGE CASE: 404 Not Found
def test_404(client):
    """
    Edge case: Controleert of de server netjes een 404-fout geeft 
    wanneer een gebruiker een pagina bezoekt die niet bestaat.
    """
    response = client.get('/niet-bestaand')   # Vraag een niet-bestaande route op
    assert response.status_code == 404        # Controleer of de statuscode exact 404 is