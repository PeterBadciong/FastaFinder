import os
import sys

def parse_fasta(fasta_file, num_sequences_per_file):
    # Create output directory
    output_dir = os.path.splitext(fasta_file)[0] + '_split'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Parse the FASTA file
    with open(fasta_file, 'r') as file:
        sequences = []
        current_seq = ""
        current_header = ""

        for line in file:
            if line.startswith(">"):  # new sequence header
                if current_header and current_seq:
                    sequences.append((current_header, current_seq))
                current_header = line.strip()
                current_seq = ""
            else:
                current_seq += line.strip()
        
        # Add the last sequence
        if current_header and current_seq:
            sequences.append((current_header, current_seq))
    
    # Split sequences into individual files
    total_sequences = len(sequences)
    file_count = 1
    for i in range(0, total_sequences, num_sequences_per_file):
        chunk = sequences[i:i + num_sequences_per_file]
        output_file = os.path.join(output_dir, f"{os.path.splitext(os.path.basename(fasta_file))[0]}_{i+1}-{i+len(chunk)}.fasta")
        
        with open(output_file, 'w') as out_file:
            for header, seq in chunk:
                out_file.write(f"{header}\n{seq}\n")
        
        print(f"Written {output_file}")
        file_count += 1

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 FastaParse.py <fasta_file> <num_sequences_per_file>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    num_sequences_per_file = int(sys.argv[2])

    parse_fasta(fasta_file, num_sequences_per_file)
