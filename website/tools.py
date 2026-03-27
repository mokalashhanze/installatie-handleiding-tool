import subprocess


class Tool:

    def __init__(self, method, input_file, output_file, refseq = None, tweaks = None):
        self.method = method
        self.refseq = refseq
        self.input = input_file
        self.output = '-o ' + output_file
        self.tweaks = tweaks

    def arguments(self):
        if self.method == "bcftools mpileup":
            arguments = [self.method, self.tweaks, self.output, "-f", self.refseq, self.input]
        else:
            arguments = [self.method, self.tweaks, self.output, self.refseq, self.input]
        
        given_arguments= []

        for item in arguments:
            if item:
                given_arguments.append(item)
        return ' '.join(given_arguments)


    def run(self):
        cmd = self.arguments()
        print(f"Running: {cmd}")
        subprocess.run(cmd, shell=True)


    def __str__(self):
        return f"method: {self.method}, input file: {self.input}, output file: {self.output}, refseq: {self.refseq}, tweaks: {self.tweaks}"



def main(kwargs):
    print("Running pipeline with:")
    print(kwargs)


    bwamem2 = Tool(
        method=f"bwa-mem2 mem -k {kwargs['k']} -w {kwargs['w']} -c {kwargs['c']}",
        refseq="GCF_000001405.40_GRCh38.p14_genomic.fna",
        input_file=kwargs["fastq_bestand"],
        output_file="output.sam"
    )


    samtools_view = Tool(
        method="samtools view",
        input_file="output.sam",
        output_file="output.bam",
        tweaks="-b"
    )

    samtools_sort = Tool(
        method="samtools sort",
        input_file="output.bam",
        output_file="sorted_output.bam"
    )


    bcftools_mpileup = Tool(
        method="bcftools mpileup",
        refseq="GCF_000001405.40_GRCh38.p14_genomic.fna",
        input_file="sorted_output.bam",
        output_file="bcftools_mpileup.bcf"
    )


    bcftools_call = Tool(
        method="bcftools call",
        input_file="bcftools_mpileup.bcf",
        output_file="out.vcf",
        tweaks="-m -O v"
    )


    pipeline = [
        bwamem2,
        samtools_view,
        samtools_sort,
        bcftools_mpileup,
        bcftools_call
    ]


    for tool in pipeline:
        tool.run()
        print(tool)

    print("Pipeline complete")
