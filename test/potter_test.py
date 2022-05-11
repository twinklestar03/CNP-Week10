from potter import *

import unittest


class PotterTest(unittest.TestCase):
    def setUp(self):
        self.potter = Potter([])
    def test_basic(self):
        self.assertEqual(self.potter.price([]), 0)
        self.assertEqual(self.potter.price([1]), 8)
        self.assertEqual(self.potter.price([2]), 8)
        self.assertEqual(self.potter.price([3]), 8)
        self.assertEqual(self.potter.price([4]), 8)
        self.assertEqual(self.potter.price([1, 1, 1]), 8 * 3)

    def test_simple_discount(self):
        self.assertEqual(8 * 2 * 0.95, self.potter.price([0, 1]))
        self.assertEqual(8 * 3 * 0.9, self.potter.price([0, 2, 4]))
        self.assertEqual(8 * 4 * 0.8, self.potter.price([0, 1, 2, 4]))
        self.assertEqual(8 * 5 * 0.75, self.potter.price([0, 1, 2, 3, 4]))

    def testSeveralDiscounts(self):
        self.assertEqual(8 + (8 * 2 * 0.95), self.potter.price([0, 0, 1]))
        self.assertEqual(2 * (8 * 2 * 0.95), self.potter.price([0, 0, 1, 1]))
        self.assertEqual((8 * 4 * 0.8) + (8 * 2 * 0.95), self.potter.price([0, 0, 1, 2, 2, 3]))
        self.assertEqual(8 + (8 * 5 * 0.75), self.potter.price([0, 1, 1, 2, 3, 4]))


    def testEdgeCases(self):
        self.assertEqual(2 * (8 * 4 * 0.8), self.potter.price([0, 0, 1, 1, 2, 2, 3, 4]))
        self.assertEqual(3 * (8 * 5 * 0.75) + 2 * (8 * 4 * 0.8), 
            self.potter.price([
                0, 0, 0, 0, 0, 
                1, 1, 1, 1, 1, 
                2, 2, 2, 2, 
                3, 3, 3, 3, 3, 
                4, 4, 4, 4
            ])
        )


if __name__ == '__main__':
    unittest.main()