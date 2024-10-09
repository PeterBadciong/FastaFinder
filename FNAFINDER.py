import os
import argparse

def combine_fna_files(parent_dir, output_file):
    # Open the output file in write mode
    with open(output_file, 'w') as outfile:
        # Traverse through all folders and files
        for root, dirs, files in os.walk(parent_dir):
            for file in files:
                # Check if the file is an .fna file
                if file.endswith('.fna'):
                    file_path = os.path.join(root, file)
                    # Open the .fna file and write its content to the output file
                    with open(file_path, 'r') as infile:
                        # Optionally, prepend the filename as a comment or sequence header if needed
                        outfile.write(f">From file: {file}\n")  # Comment this out if unnecessary
                        # Copy content
                        for line in infile:
                            outfile.write(line)

    print(f"All .fna files from {parent_dir} have been combined into {output_file}.")

if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description='Combine .fna files into a single fasta file.')
    parser.add_argument('parent_dir', type=str, help='The parent directory containing folders with .fna files.')
    parser.add_argument('output_file', type=str, help='The output fasta file.')

    # Parse the arguments
    args = parser.parse_args()

    # Run the function with provided arguments
    combine_fna_files(args.parent_dir, args.output_file)
