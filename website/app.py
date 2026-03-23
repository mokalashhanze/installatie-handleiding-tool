from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/bmf', methods=['GET', 'POST'])
def bmf():
    if request.method == 'GET':
        return render_template("bmf-get.html")
    elif request.method == 'POST':
        kwargs = {
            "fastq_bestand" : request.form['fastq_bestand'],
            "nucleotiden_achter_elkaar" : request.form['nucleotiden_achter_elkaar'],
            "afstand_matches" : request.form['afstand_matches'],
            "maximaal_keer_gerapporteerd" : request.form['maximaal_keer_gerapporteerd'],
        }
        return render_template("bmf-post.html", **kwargs)
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
