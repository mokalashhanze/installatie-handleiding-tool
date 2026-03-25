import subprocess
import time

class Tools():
    pass


def main(kwargs):
    print(kwargs)
    print(kwargs["k"])
    print(kwargs["fastq_bestand"])
    time.sleep(10)
    # # Run bwa-mem2
    # subprocess.run(
    #     f"/homes/oadogger/Desktop/toolbox/bwa-mem2-2.3_x64-linux/bwa-mem2 mem -k {kwargs['k']} -w {kwargs['w']} -c {kwargs['c']} GCF_000001405.40_GRCh38.p14_genomic.fna {kwargs['fastq_bestand']} > output.sam",
    #     shell=True
    # )
    # print("BWA-mem2")
    # #Output.bam -> output.sam
    # subprocess.run(
    #     "/homes/oadogger/Desktop/toolbox/samtools-1.23/bin/samtools view -b -o output.bam output.sam",
    #      shell=True
    # )
    # # Sort de bam file
    # subprocess.run(
    #     "/homes/oadogger/Desktop/toolbox/samtools-1.23/bin/samtools sort output.bam > sorted_output.bam",
    #     shell=True
    # )
    #
    # subprocess.run(
    #     "/homes/oadogger/Desktop/toolbox/bcftools-1.23/bcftools mpileup sorted_output.bam -f GCF_000001405.40_GRCh38.p14_genomic.fna > bcftools_mpileup.bam",
    #     shell=True
    # )
    # subprocess.run(
    #     "/homes/oadogger/Desktop/toolbox/bcftools-1.23/bcftools call -m -O v -o out.vcf bcftools_mpileup.bam",
    #     shell=True)
    print(f"done!")