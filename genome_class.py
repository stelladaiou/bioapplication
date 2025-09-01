"""genome_class.py
Author: Stella Daiou"""

from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from urllib.error import URLError

class Genome:
    """Create a class named Genome"""

    def __init__(self):
        """
        The constructor initialises the attributes as empty strings or empty lists, to store the sequence
        """
        self.seq = ""  # Initialise an empty string
        self.trial_seq = ""
        self.fasta_unchecked = ""
        self.fasta_sequence = []  # Initialise an empty list
        self.fasta = ""

    def get_sequence(self,sequence):
        """
        Store the input sequence that has been converted to uppercase into the self.trial_seq attribute
        """
        sequence = sequence.upper()  # output sequence in uppercase
        self.trial_seq=sequence

    def check_sequence(self):
        """
        Conditionals to raise errors if the DNA sequence does not include valid characters.
        """
        valid_letters = {'A', 'T', 'C', 'G'}  # define DNA nucleotides

        if 'U' in self.trial_seq: # check if U is included in the sequence
            if self.trial_seq.count('T') == 0:  # if there are no T in the sequence, then RNA sequence
                raise ValueError("The sequence you provided is an RNA sequence. Please start you search again "
                                 "and provide a DNA sequence.")
            else:
                raise ValueError("The provided sequence is not valid. Only A, T, C, G are allowed."
                                 "Please start you search again.")

        for char in self.trial_seq: # check if all characters of the DNA sequence are one of the valid letters
            if char not in valid_letters:
                raise ValueError("The provided sequence is not valid. Only A, T, C, G are allowed."
                                 "Please start you search again.")

        self.seq = self.trial_seq  # store the sequence into the self.seq attribute
        print(f'The provided DNA sequence is:\n{self.seq}\n')

    def get_seq_statistics(self):
        """
        Method to calculate the basic statistics of the sequence, i.e. length, number of A, T, G, C nucleotides
        and GC content
        """
        sequence_length = len(self.seq)
        print(f'The sequence length is: {sequence_length}')
        a_count = self.seq.count('A')
        t_count = self.seq.count('T')
        g_count = self.seq.count('G')
        c_count = self.seq.count('C')
        if sequence_length > 0:  #check if sequence is not empty to then calculate GC content
            gc_content = (g_count + c_count) / len(self.seq) * 100
        else:
            gc_content = 0
        print(f'Number of A: {a_count}')
        print(f'Number of T: {t_count}')
        print(f'Number of G: {g_count}')
        print(f'Number of C: {c_count}')
        print(f'GC Content: {gc_content:.2f}%')

    def convert_to_fasta(self):
        """
        Method to convert the DNA sequence into FASTA format.
        """
        header = ">sequence" # create the header
        self.fasta_sequence = "" # initialise an empty string
        for i in range(0, len(self.seq), 80):   # loop to cut the sequence in 80-character chunks
            self.fasta_sequence += self.seq[i:i + 80] + '\n'  # appends new lines of 80 characters long to the string
        print(f'Please find the FASTA format of your sequence below:\n {header + '\n' + self.fasta_sequence}')

    def get_fasta(self):
        """
        Method to get an input multi-line sequence in FASTA format and save it into the self.fasta attribute.
        """
        lines = []  # initialise an empty list
        # start a while loop where each line of the sequence is store in the variable line,
        # until no other lines exist
        while True:
            line = input()  # Read input line
            if line == "":  # Check for an empty line to stop input
                break
            lines.append(line)  # Append all lines to the list
        self.fasta = "\n".join(lines) # Join the list into a string, but each line is in a newline
        print(f'The provided DNA sequence is:\n{self.fasta}')

    def convert_to_plain_text(self):
        """
        Method to convert a FASTA formatted sequence into a plain text sequence.
        It takes the FASTA sequence, removes the header and concatenates the rest of sequences lines into a string.
        Then stores the string into the self.trial_seq attribute.
        """
        lines = self.fasta.splitlines()  # Split the self.fasta string into a list of lines
        self.fasta_unchecked = "".join(lines[1:])  # Concatenate the lines into a string, skipping the header
        self.trial_seq = self.fasta_unchecked  # Store the string into self.trial_seq variable
        print("\n")
        # print(self.seq)# Output the concatenated sequence

    def get_blast_results(self):
        """
        Method to send the query DNA sequence to the NCBI BLAST server and search for homologous sequences in
        the nucleotide database. It then parses the Blast results, and for each alignment it examines the HSPs
        and calculates the e-value and the percent identity. It then sorts the alignments by percent identity and
         shows the top results with the highest similarity (% identity).
        """
        print(f'Sending the sequence to NCBI for BLAST search. This may take a while...')
        try:
            result_handle = NCBIWWW.qblast("blastn", "nt", self.fasta)  # Send sequence to NCBI
            blast_record = NCBIXML.read(result_handle)  # Parse the results

            blast_results = [] # Create an empty list to store the blast results
            # for each alignment it gets the accession and the description
            for alignment in blast_record.alignments:
                accession = alignment.accession
                description = alignment.hit_def

                best_percent_identity = 0 # initialise the highest percent identity to 0
                best_e_value = float('inf') # initialise the e-value to infinity
                # loop of each HSP (High-scoring Pairs) associated with an alignment
                for hsp in alignment.hsps:
                    percent_identity = (hsp.identities / hsp.align_length) * 100 #calculate the %identity
                    if percent_identity > best_percent_identity:  # check of the %identity of the HSP is greater
                        # than the current best %identity. If so:

                        best_percent_identity = percent_identity #a better value is assigned to the best %identity
                        best_e_value = hsp.expect  # Take the e-value from the best match

                # Sort the blast results
                blast_results.append((accession, description, best_e_value, best_percent_identity))

            # Sort the results by highest percent (%)identity and store them
            results = sorted(blast_results, key=lambda x: x[3], reverse=True)

            # From the sorted results print the top 10 alignments
            print(f'\nTop BLAST Results (sorted by Percent Identity):\n')
            for i, (accession, description, e_value, percent_identity) in enumerate(results[:10], start=1):
                print(f'{i}. Accession: {accession}')
                print(f'   Description: {description}')
                print(f'   E-value: {e_value:.2e}')
                print(f'   Percent Identity: {percent_identity:.2f}%\n')

            print(f'BLAST search completed.')
        except URLError as e:  # catch an error if ii is network-related
            print(f'Network error occurred while searching in BLAST: {e}')
        except Exception as e: # catch any other type of errors
            print(f'An error occurred while searching in BLAST: {e}')
