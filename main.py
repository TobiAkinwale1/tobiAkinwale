import matplotlib.pyplot as plt


def extract_alignment_scores(sam_file):
    """
    Extracts alignment scores (AS:i: tag) from a SAM file.
    Returns a list of tuples where each tuple is (genome position, percent identity).
    Assumes that the NM tag is used to denote mismatches.
    """
    alignments = []

    with open(sam_file, 'r') as f:
        for line in f:
            if not line.startswith('@'):  # Skip header lines
                fields = line.strip().split('\t')
                genome_position = int(fields[3])  # 4th field is the 1-based leftmost mapping position
                tags = fields[11:]  # The optional fields start from the 12th field

                as_score = None
                nm_score = None

                for tag in tags:
                    if tag.startswith("AS:i:"):
                        as_score = int(tag.split(":")[2])
                    elif tag.startswith("NM:i:"):
                        nm_score = int(tag.split(":")[2])

                # Calculate percent identity: (alignment length - mismatches) / alignment length * 100
                if as_score and nm_score is not None:
                    length = as_score + nm_score
                    percent_identity = ((length - nm_score) / length) * 100
                    alignments.append((genome_position, percent_identity))

    return alignments


def generate_frp(alignments):
    """
    Generates a Fragment Recruitment Plot using the extracted alignments.
    """
    x = [a[0] for a in alignments]
    y = [a[1] for a in alignments]

    plt.scatter(x, y, s=1, c='blue')  # s sets the size of the scatter points
    plt.xlabel("Position in Genome")
    plt.ylabel("Percent Identity")
    plt.title("Fragment Recruitment Plot")
    plt.show()


if __name__ == "__main__":
    sam_file_path = "/Users/tobivalentine/Downloads/d57ae91b02581e1c4c0c-0deaa8f604b452855aff28469d60a85e23a2ef9f" \
                    "/test.sam"  # Replace with the path to your SAM file
    alignments = extract_alignment_scores(sam_file_path)
    generate_frp(alignments)
try:
    alignments = extract_alignment_scores(sam_file_path)
    generate_frp(alignments)
except FileNotFoundError:
    print(f"The file at path {sam_file_path} was not found. Please check the file path and try again.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

