import os


f1 = open("data.txt")

lines = f1.readlines()

dic = {}


for line in lines:

    key, value = line.split(",")

    dic[key] = value


for key in dic:
    print(key, dic[key])
# 2
gencode = {

    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',

    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',

    'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',

    'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',

    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',

    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',

    'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',

    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',

    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',

    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',

    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',

    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',

    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',

    'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',

    'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',

    'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W'}

protein_sequence = ''

dna_sequence = input('Enter DNA sequence: ')

for i in range(0, len(dna_sequence), 3):
    protein_sequence += gencode.get(dna_sequence[i:i + 3])

print('Protein Sequence: {}'.format(protein_sequence))
