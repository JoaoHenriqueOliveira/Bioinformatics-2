from CyclopeptideSequencing import *
import unittest

class cyclopeptides_seuqnencing_test(unittest.TestCase):

    def test_number_subpeptides(self):
        self.assertEqual(numberSubpeptides(31315), 980597910)

    def test_linear_spectrum(self):
        self.assertEqual(LinearSpectrum("NQEL"), [0, 113, 114, 128, 129, 242, 242, 257, 370, 371, 484])

    def test_cyclic_spectrum(self):
        self.assertEqual(CyclicSpectrum("NQEL"), [0, 113, 114, 128, 129, 227, 242, 242, 257, 355, 356, 370, 371, 484])

if __name__ == "__main__":
    unittest.main()
    pass
