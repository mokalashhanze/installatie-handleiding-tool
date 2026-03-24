from flask import request, render_template, Flask
from threading import Thread
import tools
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def pijplijn(**kwargs):
    tools.main2(kwargs)
@app.route('/bmf', methods=['GET', 'POST'])
def bmf():
    method = request.method
    if method == 'GET':
        return render_template("bmf-get.html", method=method)
    elif method == 'POST':
        kwargs = {
            "fastq_bestand" : request.form['fastq_bestand'],
            "k" : request.form['nucleotiden_achter_elkaar'],
            "w" : request.form['afstand_matches'],
            "c" : request.form['maximaal_keer_gerapporteerd'],
        }

        # Hiermee checken we of de file correct is, als niet word het niet door gestuurd.
        file_name = kwargs["fastq_bestand"]
        file_type = file_name.rsplit(".", 1)[-1]

        if file_type == "fastq" or file_type == "fq":
            #Hiermee beginnen we een andere thread zodat we veranderen van pagina voordat het af is om te laten zien dat
            thread = Thread(target=pijplijn, kwargs=kwargs, daemon=True)
            thread.start()

            return render_template("bmf-get.html", **kwargs, method=method)
        else:
            method = "GET"
            return render_template("bmf-get.html", **kwargs, method=method)
    return None
@app.route('/bwa-mem2')
def bwamem2():
    return render_template('bwa-mem2.html')
@app.route('/samtools')
def samtools():
    return render_template('samtools.html')
@app.route('/bcftools')
def bcftools():
    return render_template('bcftools.html')
@app.route('/contacten')
def contacten():
    return render_template('contactgegevens.html')


if __name__ == '__main__':
    app.run(debug=True)
