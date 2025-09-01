# Application for DNA sequence analysis
- [Intended Purpose](#Intended_Purpose)
- [Run the application](#Run_the_application)
- [Use Cases](#Use_Cases)
- [Thinks to be considered when running the application](#Thinks_to_be_considered_when_running_the_application)


## Intended Purpose
This DNA sequence analysis application is a tool that is designed for processing DNA sequences to be further used for 
research analysis. Its functionality enables to input the DNA sequence in multiples formats, plain text or FASTA and 
output the sequence in the most appropriate format for the user (FASTA or text respectively). It also offers analysis 
of basic statistics including sequence length, base numbers for each type of nucleotide and GC content. Additionally, 
they user can identify the sequence by searching in the NCBI BLAST database to find homologous sequences. This 
application is a useful tool for researchers that work with DNA sequences and wish to obtain quick insights into their 
data and compare their sequences with annotated sequences stored in a curated database.


## Run the application

### Prerequisites:
- Python 3.12
- The `biopython` library for analysing the sequence and the BLAST search integration.

### Installation:
The user should follow the steps below in order to run the application.

1. Download the files mentioned below into the same folder:
* genome_class.py (contains all the processing methods within the Genome class)
* cli.py (includes the running program to run the sequence analysis using the command line)
* requirements.txt (includes of required Python libraries)
2. Then install the dependencies found in the requirements.txt. using the following command:
>pip install -r requirements.txt


### Run:
1. The user can run the application by executing the cli.py in the terminal.
> python cli.py

2. Then the user can select the format type and input the DNA sequence following the prompts and conduct the 
desired analysis.




## Use Cases
### Example case 1:
The example below provides a step-by-step guidance to help the user use the application when analysing a FASTA formatted 
sequence. The example sequence will be used for this case can be found in the fasta_sequence.txt and is the DNA sequence
of the Chlamydia Trachomatis plasmid.


#### Task 1
First the user will be asked to choose the format type of the sequences. In this case, the user should type FASTA, 
and press Enter.

#### Task 2 
Then the application confirms that the FASTA format was selected and ask for the input DNA sequence. At this point 
the user should provide the input sequence in FASTA format and press Enter. 

The application processes the input DNA sequence by displaying the provided sequence, eg the first rows of the seq:\
The provided DNA sequence is:
AAGTTATTTCTGAATGAGTACTGCGCTCCTTTTTATGACATCTGCATAATAGACACTCCA
CCTAGCCTAGGAGGGTTAACGAAAGAAGCTTTTGTTGCAGGAGACAAATTAATTGCTTGT
TTAACTCCAGAACCTTTTTCTATTCTAGGGTTACAAAAGATACGTGAATTCTTAAGTTCG
GTCGGAAAACCTGAAGAAGAACACATTCTTGGAATAGCTTTGTCTTTTTGGGATGATCGT....

#### Task 3
Then the application asks the user to select one of the three options by typing 1, 2, or 3:
1. Search your sequence in Blast
2. Calculate the basic statistics of your sequence 
3. Do both\
In this case, we type 2 to calculate the basic statistics of the sequence. To do that, the application first converts
the FASTA formatted sequence to plain text and then calculates the length of the sequence, base number per nucleotide
and the GC content(%). 

The expected results of the analysis are the following:

The sequence length is: 7553\
Number of A: 2476\
Number of T: 2336\
Number of G: 1448\
Number of C: 1293\
GC Content: 36.29%

Then the application finishes the analysis and provides the following message to the user:\
Thanks for using the app. See you next time!


### Example case 2:
The example below provides a step-by-step guidance to help the user when using a plain text sequence. The example 
sequence will be used for this case is the following:\
CTTTCCAGTTTTGAACGGAAGATATTTCCTTTTTCACCATAGCCCTCTATGGGCTTCCAAATATCCCTTTGCCAATTCCACAAGAACAGCCTTAGCGAAAGG

#### Task 1
First the user will be asked to choose the format type of the sequences. In this case, the user should type Text, 
and press Enter.

#### Task 2
Then the application confirms that the Text format was selected and ask for the input DNA sequence. At this point 
the user should provide the input sequence in Text and press Enter. 

The application processes the input DNA sequence by displaying the provided sequence, eg:\
The provided DNA sequence is:
CTTTCCAGTTTTGAACGGAAGATATTTCCTTTTTCACCATAGCCCTCTATGGGCTTCCAAATATCCCTTTGCCAATTCCACAAGAACAGCCTTAGCGAAAGG

#### Task 3
Then the application asks the user to select one of the three options by typing 1, 2, or 3:
1. Calculate the basic statistics of your sequence
2. Convert to FASTA format
3. Do both\

In this case, we type 3 to calculate the basic statistics of the sequence and then convert it to Fasta format. 
The application first calculates the statistics displayed below:\
The sequence length is: 102\
Number of A: 27\
Number of T: 31\
Number of G: 16\
Number of C: 28\
GC Content: 43.14%

Then it displays the FASTA format:
Please find the FASTA format of your sequence below:
 '>sequence
CTTTCCAGTTTTGAACGGAAGATATTTCCTTTTTCACCATAGCCCTCTATGGGCTTCCAAATATCCCTTTGCCAATTCCA
CAAGAACAGCCTTAGCGAAAGG'

#### Task 4
Now the user is asked to either continue with performing BLAST analysis or end the analysis, showing the following:#\
Do you want to further search your sequence in Blast?:
1. Yes
2. No

Please type Y or N, then press Enter:\
The user now should type Y to search in BLAST.

#### Task 5
The application will compare the input sequence with the sequences found in the NCBI BLAST and will try and find the
homologous sequences. If there are any, the application will display the 10 top BLAST results ranked by the percent
identity.
As long as the application retrieves data from the NCBI server, the user will be seeing the following message:
"Sending the sequence to NCBI for BLAST search. This may take a while..."

Once this process is finished, the application will display the results providing the description of the homologous 
sequence, the e-value and the percent identity(%). If there are more hits assigned to a specific homologue, it will
include this as well.

In this case, the sequence is just a random group of bases, therefore the application will display the following 
message:
An error occurred while searching in BLAST: Error message from NCBI: Message ID#29 Error: Query string not 
found in the CGI context

At the end, the application thanks the user for using the app.




### Thinks to be considered when running the application
#### Error raising with wrong formatted input sequence
1. If the user selects the Text format but then provides a FASTA formatted sequence, a ValueError will be raised 
stating:The provided sequence is not valid. Only A, T, C, G are allowed.Please start you search again.
The same wll happen if the user provides a sequence that has invalid characters other than A, T, C, G. 
2. In the case where the sequence is an RNA sequence, i.e. all T nucleotides are replaced by U, then the error will be
the following:The sequence you provided is an RNA sequence. Please start you search again and provide a DNA sequence.
3. In any case of wrong input the application will raise an error and then the user should start the analysis from 
scratch.

#### Display the same question if wrong character is pressed
1. For any multiple choice questions, if the user accidentally press a wrong character other than the choices, 
then the question will be repeated until the user selects one of the available options. Including while loops in the 
cli.py enable the user to continue running the analysis without any issues.

#### Errors when running BLAST
1. Although Blast is a valuable database that provides a lot of options on analysing our data, often the NCDBI
servers are temporarily unavailable. For this reason, a URLError was included to inform the user about the connection
issues with NCBI server. It is a helpful informative error for the user not to assume that the application is not 
working or that the sequence is not a valid sequence.
2. If the sequence provided does not match with any of the sequences found in Blast, then the following error will be 
displayed: "An error occurred while searching in BLAST:"

#### Notes
1. Some of the methods cannot be tested in the test_genome_class.py
2. Unlike Text format, when a wrong sequence or format is provided for FASTA, the application will keep running, 
however, this was not the indented purpose. The purpose was to check the quality of the sequence and not further let
the user proceed of the sequence is not valid.

### Conclusion
This completes the testing of the DNA sequence analysis application.




