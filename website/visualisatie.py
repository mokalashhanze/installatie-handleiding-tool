"""

"""

import matplotlib.pyplot as plt


def read_file(filename):
    """
    this function reads the file, skips all of the metadata and filters every line to contain
    only the information that is useful for making a plot, in this case the chromosome and the
    information about the match
    :param filename: a string with the name of the file
    :return: file_lines: all of the not-metadata lines in the file, filtered by useful info
    """
    # for different information in the final list, change the desired info in useful_info
    useful_info = ['#CHROM', 'INFO']
    file_lines = []
    info_indices = []
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('##'):
                # skips metadata
                continue

            elif line.startswith('#'):
                # takes the line starting with #chrom
                index_line = line.strip().split('\t')

                for position, index_item in enumerate(index_line):
                    if index_item in useful_info:
                        info_indices.append(position)
                continue

            # only keeps the useful columns
            list_of_line = line.strip().split('\t')
            selected_lines = []
            for indexed_position in info_indices:
                selected_lines.append(list_of_line[indexed_position])

            file_lines.append(selected_lines)
    return useful_info, file_lines


def datafilter(mutation_lines, index_line):
    """
    this function filters the data to only contain the lines with indels and snp's.
    :param mutation_lines:
    :param index_line:
    :return:
    """
    info_position = 0
    chrom_position = 0

    for position, item in enumerate(index_line):
        if item == '#CHROM':
            chrom_position = position
        elif item == 'INFO':
            info_position = position

    indels_and_snps = {}

    for subline in mutation_lines:
        chrom_in_mutation_lines = subline[chrom_position]
        if chrom_in_mutation_lines not in indels_and_snps:
            indels_and_snps[chrom_in_mutation_lines] = {'INDEL':0, 'SNP':0}


        if 'INDEL' in subline[info_position]:
            indels_and_snps[chrom_in_mutation_lines]['INDEL'] += 1
        if 'SNP' in subline[info_position]:
            indels_and_snps[chrom_in_mutation_lines]['SNP'] += 1
    return indels_and_snps


def plot_maker(indels_and_snps):
    """
    :return:
    """
    found_mutations = {}
    chromosomes = []
    indels = []
    snps = []
    for key in indels_and_snps:
        if indels_and_snps[key]['INDEL'] == 0 and indels_and_snps[key]['SNP'] == 0:
            continue
        else:
            chromosomes.append(key)
            indels.append(indels_and_snps[key]['INDEL'])
            snps.append(indels_and_snps[key]['SNP'])

    fig,ax = plt.subplots()
    ax.set_title('mutations per chromosome')
    ax.set_xlabel('chromosome')
    ax.set_ylabel('mutations')
    ax.bar(chromosomes, indels, label='indels')
    ax.bar(chromosomes, snps, bottom=indels, label='snps')
    ax.legend(loc='upper left')
    fig.savefig('static/pictures/mutations_per_chromosome.png')


def main():
    # chromosome_dict = {
    #     'NC_000001.11': 1, 'NC_000002.12': 2, 'NC_000003.12': 3,
    #     'NC_000004.12': 4, 'NC_000005.10': 5, 'NC_000006.12': 6,
    #     'NC_000007.14': 7, 'NC_000008.11': 8, 'NC_000009.12': 9,
    #     'NC_000010.11': 10, 'NC_000011.10': 11, 'NC_000012.12': 12,
    #     'NC_000013.11': 13, 'NC_000014.9': 14, 'NC_000015.10': 15,
    #     'NC_000016.10': 16, 'NC_000017.11': 17, 'NC_000018.10': 18,
    #     'NC_000019.10': 19, 'NC_000020.11': 20, 'NC_000021.9': 21,
    #     'NC_000022.11': 22, 'NC_000023.11': 'X', 'NC_000024.10': 'Y',
    #     'NC_012920.1': 'MT'
    # }

    index_line, mutation_lines = read_file('out.vcf')

    indels_and_snps = datafilter(mutation_lines, index_line)
    plot_maker(indels_and_snps)


if __name__ == '__main__':
    main()
