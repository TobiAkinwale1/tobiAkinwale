import sys
import gzip


def read_fasta(file_name):
    with (gzip.open(file_name, 'rt') if file_name.endswith('.gz') else open(file_name, 'r')) as file:
        sequences = []
        sequence = ""
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if sequence:
                    sequences.append(sequence)
                    sequence = ""
            else:
                sequence += line
        if sequence:  # Add the last sequence
            sequences.append(sequence)
    return sequences


def count_residues(sequences, count_stops=True):
    total_residues = sum(len(seq) for seq in sequences)
    if not count_stops:
        total_residues -= sum(seq.count('*') for seq in sequences)
    return total_residues


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fasta_stats.py <path_to_fasta_file>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    sequences = read_fasta(fasta_file)

    print("Total sequences found:", len(sequences))
    print("Total residues found (counting *):", count_residues(sequences))
    print("Total residues found (excluding *):", count_residues(sequences, count_stops=False))
