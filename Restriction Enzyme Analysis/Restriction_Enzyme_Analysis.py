# This Python script performs a restriction enzyme analysis on a DNA sequence provided in a FASTA file

import sys  # Import the sys module to handle command-line arguments

# Function to read and extract information from a FASTA file
def read_fasta(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()  # Read all lines from the file
        header = lines[0][1:].strip()  # Get the sequence header (omit the '>' character)
        sequence = ''.join(line.strip() for line in lines[1:])  # Concatenate sequence lines into one string
    return header, sequence

# Function to read and extract information from the enzyme file
def read_enzymes(filename):
    with open(filename, 'r') as file:
        enzymes = {}
        for line in file:
            name, sequence = line.strip().split(';')  # Enzymes file format: name;cut_site
            if '^' in sequence:  # Ensure the enzyme cut site is valid (contains a '^' indicating the cut site)
                enzymes[name] = sequence
            else:
                raise ValueError("Invalid format in enzyme file. Missing '^' in cut site sequence.")
    return enzymes

# Function to cut the DNA sequence at enzyme cut sites
def cut_sequence(sequence, enzyme, name, seq_position):
    fragments = []  # List to store sequence fragments
    pos = sequence.find(enzyme.replace('^', ''))  # Find the first occurrence of the enzyme sequence

    # Iterate through all cutting sites in the sequence
    while pos != -1:
        cut_pos = pos + enzyme.index('^')  # Find the cutting position (where '^' occurs in enzyme)
        fragments.append(sequence[:cut_pos])  # Append the fragment before the cut
        sequence = sequence[cut_pos:]  # Update the sequence to the remaining part after the cut
        pos = sequence.find(enzyme.replace('^', ''))  # Find the next occurrence of the enzyme
        seq_position += len(fragments[-1]) + 1  # Update the sequence position

    fragments.append(sequence)  # Append the last fragment (after the final cut)

    # Display cut results
    print(f"There are {len(fragments) - 1} cutting sites for {name}, cutting at {enzyme}")
    
    if len(fragments) > 1:
        print(f"There are {len(fragments)} fragments:")

        # Iterate through fragments and format them for display
        for i, fragment in enumerate(fragments, 1):
            print(f"Length- {len(fragment)}")
            # Group the fragment into blocks of 10 characters for readability
            grouped_fragment = [fragment[j:j + 10] for j in range(0, len(fragment), 10)]
            # Further group into lines of 6 blocks
            lines = [' '.join(grouped_fragment[k:k + 6]) for k in range(0, len(grouped_fragment), 6)]
            for line in lines:
                print(f"{seq_position} {line}")
                seq_position += len(line)  # Update sequence position for each line
    else:
        print("No cutting sites found.")

# Main entry point of the script
if __name__ == '__main__':
    # Ensure the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python3 script.py <fasta_file> <enzyme_file>")
        sys.exit(1)

    # Get the filenames from the command-line arguments
    fasta_filename = sys.argv[1]
    enzyme_filename = sys.argv[2]

    # Print output header
    print(f"Restriction enzyme analysis of sequence from file {fasta_filename}.")
    print(f"Cutting with enzymes found in file {enzyme_filename}.")
    print("\n---------------------------------------------------------------\n")

    # Read the FASTA sequence and enzyme data
    header, sequence = read_fasta(fasta_filename)
    print(f"Sequence name: {header}")
    print(f"Sequence is {len(sequence)} bases long.")
    print("\n---------------------------------------------------------------\n")

    enzymes = read_enzymes(enzyme_filename)

    # Initialize sequence position (1-based index for display)
    seq_position = 1

    # Loop through each enzyme and perform sequence cutting
    for name, site in enzymes.items():
        cut_sequence(sequence, site, name, seq_position)
        print("\n---------------------------------------------------------------\n")

