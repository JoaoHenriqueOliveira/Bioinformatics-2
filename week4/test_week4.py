from CyclopeptideScoring import *
from SpecctralConvolution import *
import unittest


class week4_test(unittest.TestCase):
    def test_cyclopeptide_scoreing(self):
        self.assertEqual(CycloPeptideScoring("NQEL", [0, 99, 113, 114, 128, 227, 257,
                                                      299, 355, 356, 370, 371, 484]), 11)

    def test_spectral_convolution(self):
        self.assertEqual(SpectralConvolution([0, 137, 186, 323]), [137, 137, 186, 186, 323, 49])
        

if __name__ == "__main__":
    unittest.main()
    pass
