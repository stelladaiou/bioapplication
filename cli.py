"""cli.py
Author: Stella Daiou"""

from genome_class import Genome

sequence = Genome()
condition_1 = True
fasta_input = []

while True:# loop that search for Text of FASTA. if not the correct answer is given, it will repeat the question
    option = input("You can enter your DNA sequence in one of the following formats:\n"
                   "1. Text\n"
                   "2. FASTA\n"
                   "Please select the format. Type Text or FASTA and press Enter:")
    if option == "Text" or option == "FASTA": # breaks the loop if Text or FASTA are found
        condition_1 = False
        break
    else:
        print("Please enter one of the available options") # prints comment to correct input
if option == "Text": # Text provided by the user
                         # use methods for Text sequence
    input_text_sequence = input("You selected Text format. Please enter your DNA sequence below and "
                               "then press Enter:\n")
    sequence.get_sequence(input_text_sequence)
    sequence.check_sequence()
    condition_followup_text = True # ask they user of they want to convert to FASTA, or get the stats, or both
    print("\nNow what do you want to do with the sequence? Please select one of the following options:\n")
    while True: # loop that search for options 1, 2 or 3. if wrong number is entered, the question will be repeated
        options_followup_text = input("1. Calculate the basic statistics of your sequence\n"
                                      "2. Convert to FASTA format\n"
                                      "3. Do both\n"
                                      "Please type 1, 2 or 3 to choose your option here. Then press Enter:")
        if options_followup_text == "1" or options_followup_text == "2" or options_followup_text == "3":
            condition_followup_text = False
            break
        else:
            print("\nPlease enter one of the available options")
    if options_followup_text == "1":
        sequence.get_seq_statistics()
        print("Thanks for using the app. See you next time!")
    elif options_followup_text == "2":
        sequence.convert_to_fasta()
        condition_followup_text_fasta = True
        while True:# ask they user of they want to search in Blast
                search_blast_option1 = input("Do you want to search your sequence in Blast?:\n"
                                             "1. Yes\n"
                                             "2. No\n"
                                             "Please type Y or N, then press Enter:")
                if search_blast_option1 == "Y" or search_blast_option1 == "N":
                    condition_followup_text_fasta = False
                    break
                else:
                    print("\nPlease enter one of the available options")
        if search_blast_option1 == "Y":
            sequence.get_blast_results()
        elif search_blast_option1 =="N":
            print("Thanks for using the app. See you next time!")
    elif options_followup_text == "3":
        sequence.get_seq_statistics()
        sequence.convert_to_fasta()
        condition_followup_text_fasta = True
        while True:# loop that search for Y and N. if not the correct answer is given, it will repeat the question
            search_blast_option1 = input("Do you want to further search your sequence in Blast?:\n"
                                             "1. Yes\n"
                                             "2. No\n"
                                             "Please type Y or N, then press Enter:")
            if search_blast_option1 == "Y" or search_blast_option1 == "N":
                condition_followup_text_fasta = False
                break
            else:
                print("\nPlease enter one of the available options")
        if search_blast_option1 == "Y":
            sequence.get_blast_results()
            print("Thanks for using the app. See you next time!")
        elif search_blast_option1 == "N":
            print("Thanks for using the app. See you next time!")

elif option == "FASTA":# FASTA provided by the user
    # use methods for Text sequence
    input_sequence = input("You selected FASTA format. Please enter your DNA sequence below and press Enter:\n")
    sequence.get_fasta()
    condition_followup_fasta = True  # ask they user of they want to search in Blast or calculate the stats
    print("\nWhat would you like to do with the sequence? Please select one of the following options:\n")
    while True:  # loop that search for options 1 or 2. if wrong number is entered, the question will be repeated
        options_followup_fasta = input("1. Search your sequence in Blast:\n"
                                       "2. Calculate the basic statistics of your sequence\n"
                                       "3. Do both\n"
                                       "Please type 1, 2, or 3 to choose your option here. Then press Enter:")
        if options_followup_fasta == "1" or options_followup_fasta == "2" or options_followup_fasta == "3":
            condition_followup_text = False
            break
        else:
            print("\nPlease enter one of the available options")
    if options_followup_fasta == "1":
        sequence.get_blast_results()
        print("Thanks for using the app. See you next time!")
    elif options_followup_fasta == "2":
        sequence.convert_to_plain_text()
        sequence.check_sequence()
        sequence.get_seq_statistics()
        print("Thanks for using the app. See you next time!")
    elif options_followup_fasta == "3":
        sequence.convert_to_plain_text()
        sequence.check_sequence()
        sequence.get_seq_statistics()
        sequence.get_blast_results()
        print("Thanks for using the app. See you next time!")
