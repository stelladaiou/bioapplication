"""test_genome_class.py
Author: Stella Daiou"""

import unittest
from unittest.mock import patch

from genome_class import Genome

class TestGenome(unittest.TestCase):
    def setUp(self):
        self.genome = Genome()  # Initialize a Genome list

    def test_get_sequence(self):
        """
        Tests if the sequence can be been converted to uppercase. It compares the input from the get_sequence
        method with the expected output
        """
        self.genome.get_sequence("gcggggtagaatgtgcctagaaagattgtagttgt")
        self.assertEqual(self.genome.trial_seq, "GCGGGGTAGAATGTGCCTAGAAAGATTGTAGTTGT")

    def test_correct_sequence(self):
        """
        Tests the correct sequence by comparing the input sequence with the expected output.
        """
        self.genome.trial_seq = "GTAGGTTCAATGCCTGCAATCTTAGAAA"
        self.genome.check_sequence()
        self.assertEqual(self.genome.seq, "GTAGGTTCAATGCCTGCAATCTTAGAAA")

    def test_rna_raising_error(self):
        """
        Tests that an error will be raised of the input sequence is an RNA sequence.
        """
        self.genome.trial_seq = "AUGCGUACGUAUUUUUU"
        with self.assertRaises(ValueError):
            self.genome.check_sequence()

    def test_mixed_ut_raising_error(self):
        """
        Tests that an error will be raised of the input sequence has both T and U nucleotides
        """
        self.genome.trial_seq = "ATGCGUACGTAGCUUUUUUUTTTTTTTT"
        with self.assertRaises(ValueError):
            self.genome.check_sequence()

    def test_invalid_character_raising_error(self):
        """
        Tests if an error will be raised with non-valid sequence
        """
        self.genome.trial_seq = "GTAGGTTCAA!!!!££$%^&LSNKDL"
        with self.assertRaises(ValueError):
            self.genome.check_sequence()

    def test_get_seq_statistics(self):
        """
        Tests the statistics of the provided DNA sequence
        """
        self.genome.seq = "GTAGGTTCAATGCCTGCAATCTTAGAAAAAAAAAA"
        with patch('builtins.print') as mocked_print:  # Capture the printed output to replace the print function
            self.genome.get_seq_statistics()

        # check if the expected output is printed
        mocked_print.assert_any_call("The sequence length is: 35")  # check if the expected output is printed
        mocked_print.assert_any_call("Number of A: 16")
        mocked_print.assert_any_call("Number of T: 8")
        mocked_print.assert_any_call("Number of G: 6")
        mocked_print.assert_any_call("Number of C: 5")
        mocked_print.assert_any_call("GC Content: 31.43%")




if __name__ == '__main__':
    unittest.main()
