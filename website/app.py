from flask import request, render_template, Flask, send_file
from threading import Thread
import tools
import os
import visualisatie

app = Flask(__name__)

# Globale status
job_status = "idle"
kwargs = {}
vorige_kwargs = {}

@app.route('/')
def home():
    return render_template('index.html')

def pijplijn(**kwargs):
    global job_status
    tools.main(kwargs)
    visualisatie.main()
    job_status = "done"

@app.route('/bmf', methods=['GET', 'POST'])
def bmf():
    global job_status, kwargs, vorige_kwargs

    # GET
    if request.method == 'GET':
        #Pijplijn draait nog
        if job_status == "running":
            return render_template("bmf-get.html",method="STATUS",status="running",**kwargs)

        #Pijplijn is klaar
        if job_status == "done":
            # Vorige_kwargs opslaan om te laten zien onder aan de input pagina voor al is de gebruiker te snel weggegaan
            vorige_kwargs = kwargs
            vorige_kwargs["output"] = "out.vcf"
            # Job_status resetten voor volgende keer user gebruik en kwargs
            job_status = "idle"
            kwargs = {}
            return render_template("bmf-get.html",method="STATUS",status="done", **vorige_kwargs)

        return render_template("bmf-get.html", method="GET", vorige=vorige_kwargs)

    # ---------------- POST ----------------
    elif request.method == 'POST':
        kwargs = {
            "fastq_bestand": request.form['fastq_bestand'],
            "k": request.form['nucleotiden_achter_elkaar'],
            "w": request.form['afstand_matches'],
            "c": request.form['maximaal_keer_gerapporteerd'],
        }

        file_name = kwargs["fastq_bestand"]
        file_type = file_name.rsplit(".", 1)[-1]

        if file_type not in ("fastq", "fq"):
            return render_template("bmf-get.html", method="GET", **kwargs)

        job_status = "running"

        thread = Thread(target=pijplijn, kwargs=kwargs, daemon=True)
        thread.start()

        return render_template("bmf-get.html", method="STATUS", **kwargs)
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

@app.route('/bmf/download')
def download_all():
    file_path = os.path.join(app.root_path, "output", "out.vcf")
    return send_file(file_path,as_attachment=True,download_name="out.vcf")

@app.route('/bmf/download2')
def download_mutaties():
    file_path = os.path.join(app.root_path, "output", "mutations_per_chromosome_dict.txt")
    return send_file(file_path,as_attachment=True,download_name="mutations_per_chromosome_dict.txt")

#output/mutations_per_chromosome_dict.txt


if __name__ == '__main__':
    app.run(debug=True)
