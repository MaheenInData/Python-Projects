# Restriction Enzyme Analysis Script

This Python script performs a restriction enzyme analysis on a DNA sequence provided in a FASTA file. The script reads a FASTA sequence and cuts it at specified enzyme recognition sites defined in a separate enzyme file. The output includes the number of cutting sites and the resulting DNA fragments.

## Features
+ Reads a DNA sequence from a FASTA file.
+ Reads restriction enzyme cut sites from a separate enzyme file.
+ Simulates the cutting of the DNA sequence at each enzyme recognition site.
+ Outputs the number of cutting sites and the lengths of the resulting fragments.

## Prerequisites
+ Python 3.x

## Installation

``` bash
git clone https://github.com/yourusername/restriction-enzyme-analysis.git
cd restriction-enzyme-analysis
```

## Usage
### FASTA File Format
The FASTA file should contain a DNA sequence in the following format:

``` shell
>sequence_name
ACTGACTGACTG...
```
+ The first line is the sequence header (starts with >).
+ The remaining lines contain the DNA sequence.

### Enzyme File Format
The enzyme file should contain restriction enzyme names and their recognition sequences in the following format:

``` css
EnzymeName;A^CTG
Enzyme2;GG^CC
```
+ Each line represents a different enzyme.
+ The recognition sequence must include a ^ symbol where the cut occurs.

### Running the Script
``` bash
python3 script.py <fasta_file> <enzyme_file>
```

## Example Output

``` bash
Restriction enzyme analysis of sequence from file example.fasta.
Cutting with enzymes found in file enzymes.txt.

---------------------------------------------------------------

Sequence name: ExampleSequence
Sequence is 5000 bases long.

---------------------------------------------------------------

There are 2 cutting sites for EnzymeName, cutting at A^CTG
There are 3 fragments:
Length- 100
1 ACTGACTGAC...
...

---------------------------------------------------------------
```




