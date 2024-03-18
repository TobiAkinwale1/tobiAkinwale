import os
import re

fasta_file_path = input("Enter FASTA file name: ")  # Tobi Noor and Irina
file = open(fasta_file_path, 'r')
descriptor = file.readlines()
for line in descriptor:
    if ">" == line[0]:
        header = line[0:6]
        print('The header is: ', header)
print()
# check if file exists
if not os.path.isfile(fasta_file_path):
    print("Please enter a valid FASTA file name")
    exit(1)

# stores sequence
seq = ""

# open the file
with open(fasta_file_path) as file:
    # check if it is valid fasta file
    if file.readline()[0] != ">":
        print("It an invalid FASTA file")
        exit(1)

    # if it is valid FASTA file
    else:
        # read the sequence
        for line in file:
            seq += line.strip()


def getReverseComplement(seq):  # Tobi
    revSeq = seq[::-1]
    complementaryBases = ["G", "C", "C", "A", "T", "T", "A"]
    return "".join([complementaryBases[base] for base in revSeq])


def reverse(seq):  # All members
    return seq[::-1]


def complement(seq):  # Noor and Irina and Tobi
    complement_dict = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
    seq_list = list(seq)
    seq_list = [complement_dict[base] for base in seq_list]
    return ''.join(seq_list)


def reverse_complement(seq):  # All members
    seq = reverse(seq)
    seq = complement(seq)
    return seq


def get_frame(seq, pos, complement):  # Tobi
    frame_length = len(seq) / 3
    if pos <= frame_length:
        frame = 1
    elif pos <= frame_length * 2:
        frame = 2
    else:
        frame = 3
    if complement == 1:
        frame += 3
    return frame


def split_sequence(seq, frame, block_size=3):  # Irina and Noor Tobi
    """Split the sequence in block of block size
    :param seq: sequence
    :param frame:
    :param block_size
    :return: list of sub sequence"""
    sequences = list()
    block = ''
    frame_part = seq[frame:]
    for index in range(len(frame_part)):
        block += frame_part[index]
        if len(block) == block_size:
            sequences.append(block)
            block = ''
    return sequences


def get_orf(codons):  # Tobi
    """Find the orf list
    :param codons:
    :return:"""
    orf = list()
    for codon in codons:
        orf.append(codon)
        if codon in ['TAA', 'TAG', 'TGA']:
            return orf


num_orfs = input('Enter the minimum ORF to search for: ')  # All
# Try to cast it to a number
num_orfs = int(num_orfs)


def analyze_sequence(seq, min_orf, reverse=False):  # Tobi and Noor and Irina
    """Analyze the sequence
    :param min_orf:
    :param sequence: sequence to analyze
    :param reverse: Trigger to analyze the reverse complement
    :return:"""
    if reverse:
        sequence = reverse_complement(seq)
        for pos in range(len(sequence) - 3):
            f = split_sequence(sequence, pos)
            if f[0] == 'ATG':
                orf = get_orf(f)
                orf2 = ''.join(map(str, orf))
                orf3 = [orf2[i:i + 3] for i in range(0, len(orf2), 3)]
                orf4 = ''.join(str(orf3).split(','))
                orf5 = orf4.replace("'", ' ')
                orf6 = str(orf5)
                if orf and len(orf) >= num_orfs:
                    print(header + f'|FRAME={get_frame(seq, pos, complement)} POS={pos} LEN = {len(orf)} \n{orf5}')


print(analyze_sequence(seq, 2, True))
