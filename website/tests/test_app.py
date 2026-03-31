import pytest
from app import app
from tools import Tool

@pytest.fixture
#def client():
   # """
    #Zet Flask-app in testmodus en maakt een testclient aan.
   # Hiermee kunnen we requests naar de server sturen zonder de app te draaien.
    #"""
    #app.config['TESTING'] = True  # Activeer de testomgeving 
    #return app.test_client()

# 1. Werkt de website?
def test_website(client):
    """
    Controleert of de website werkt
    """
    response = client.get('/')      # Voer een GET-request uit op de home pagina(index.html)
    assert response.status_code == 200  # Controleer of de server 200 (OK) teruggeeft

# 2. DYNAMISCHE PAGINA:
def test_DYNAMISCHE_valid(client):
    """
    Test of de dynamische pagina werkt
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
    Test of de Tool-class een correcte leesbare string geeft.
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
    Test de 'view' methode van de samtools met variabelen.
    """
    # Stap 1: Definieer je test-waarden
    test_input = "input.sam"
    test_output = "output.bam"
    test_flag = "-b"  
    # Stap 2: Maak het Tool-object aan met de variabelen
    test_tool = Tool(                 
        method="samtools view",
        input_file=test_input,
        output_file=test_output,
        tweaks=test_flag
    )
    # Stap 3: Haal de argumenten op
    args = test_tool.arguments()   
    # Stap 4: Controleer of de variabelen op de juiste plek staan
    assert "samtools view" in args    
    assert test_flag in args              
    assert f"-o {test_output}" in args 
    assert test_input in args

# 6. TEST bcftools mpileup 
def test_bcftools_mpileup_arguments():
    """
    Test de mpileup van de bcftools met variabelen voor bestandspaden.
    """
    # 1. Definieer de variabelen
    methode = "bcftools mpileup"
    referentie = "referentie/genome.fna"
    input_bam = "output/sorted.bam"
    output_bcf = "output/mpileup.bcf"

    # 2. Maak het Tool object aan
    bcftools_mpileup = Tool(       
        method=methode,
        refseq=referentie,
        input_file=input_bam,
        output_file=output_bcf
    )
    
    args = bcftools_mpileup.arguments()      

    # 3. Asserties met de variabelen
    assert methode in args         
    assert f"-f {referentie}" in args 
    assert f"-o {output_bcf}" in args   
    assert input_bam in args

# 7. EDGE CASE: Verkeerd bestandstype 
def test_ongeldig_bestanden(client):
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
    assert response.status_code == 200
    assert b"Verkeerde file" in response.data    

# 8. EDGE CASE: lege velden
def test_lege_velden(client):
    """
    controleert hoe de website regeart op de lege velden
    """
    payload = { 
        "fastq_bestand": "", 
        "nucleotiden_achter_elkaar": "19", # Dit wordt 'k' in je app.py
        "afstand_matches": "100",
        "maximaal_keer_gerapporteerd": "500"
    } 
    
    response = client.post('/bmf', data=payload)
    assert response.status_code == 200
    assert b"Geen file, upload een file!" in response.data