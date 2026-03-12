from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/bmf')
def bmf():
    return render_template('bmf.html')
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
    app.run()
