import subprocess

class Tools():
    pass


def main():
    subprocess.run(f"bwa-mem2 mem GCF_000001405……fna sequence_test.fastq > output.bam")
    subprocess.run("samtools view -b -o samtools_test.bam output.sam")
    subprocess.run("samtools sort samtoolstest.bam > sorted_samtools.bam")
    subprocess.run("bcftools mpileup sorted_samtools.bam -f GCF_000001405.40…..fna > bcftools_mpileup.bam")
    subprocess.run("bcftools call -m -O v -o out.vcf bcftools_mpileup.bam")

def main2(kwargs):
    print(kwargs)
    print(kwargs["k"])
    print(kwargs["fastq_bestand"])

    #subprocess.run(f"bwa-mem2 mem -k {kwargs["k"]} -w {kwargs["w"]} -c {kwargs["c"]}  INDEX-BESTAND {"fastq-bestand"} > output.bam")
    #subprocess.run("samtools view -b -o samtools_test.bam output.sam")
    #subprocess.run("samtools sort samtoolstest.bam > sorted_samtools.bam")
    #subprocess.run("bcftools mpileup sorted_samtools.bam -f GCF_000001405.40…..fna > bcftools_mpileup.bam")
    #subprocess.run("bcftools call -m -O v -o out.vcf bcftools_mpileup.bam")
    print(f"done!")