# -*- coding: utf8 -*-

import unittest
import random
import basic_math as bm


class TestBasicMath(unittest.TestCase):
    def test_get_greatest(self):
        random_number_list = [95, 61, 96, 45, 27, 86, 33, 66, 4, 39]
        pred = bm.get_greatest(random_number_list)
        self.assertEqual(pred, 96)

        random_number_list = [21, 83, 49, 11, 73, 57, 55, 47, 9, 30]
        pred = bm.get_greatest(random_number_list)
        self.assertEqual(pred, 83)

        random_number_list = [85, 19, 30, 39, 91, 81, 76, 47, 5, 26]
        pred = bm.get_greatest(random_number_list)
        self.assertEqual(pred, 91)

        random_number_list = [10, 15, 47, 3, 11, 60, 51, 17, 1, 77]
        pred = bm.get_greatest(random_number_list)
        self.assertEqual(pred, 77)

        random_number_list = [19, 35, 4, 21, 29, 87, 32, 10, 53, 63]
        pred = bm.get_greatest(random_number_list)
        self.assertEqual(pred, 87)

        random_number_list = [66, 86, 81, 94, 23, 8, 30, 52, 27, 89]
        pred = bm.get_greatest(random_number_list)
        self.assertEqual(pred, 94)

        random_number_list = [4, 40, 59, 45, 28, 2, 98, 39, 63, 27]
        pred = bm.get_greatest(random_number_list)
        self.assertEqual(pred, 98)

        random_number_list = [35, 16, 69, 40, 27, 49, 59, 48, 66, 1]
        pred = bm.get_greatest(random_number_list)
        self.assertEqual(pred, 69)

        random_number_list = [44, 67, 72, 57, 84, 86, 16, 14, 65, 61]
        pred = bm.get_greatest(random_number_list)
        self.assertEqual(pred, 86)

        random_number_list = [42, 46, 56, 98, 60, 48, 21, 15, 64, 81]
        pred = bm.get_greatest(random_number_list)
        self.assertEqual(pred, 98)

    def test_get_smallest(self):
        random_number_list = [67, 78, 66, 40, 4, 95, 30, 84, 10, 28]
        pred = bm.get_smallest(random_number_list)
        self.assertEqual(pred, 4)

        random_number_list = [75, 40, 5, 45, 14, 17, 35, 37, 57, 21]
        pred = bm.get_smallest(random_number_list)
        self.assertEqual(pred, 5)

        random_number_list = [53, 23, 77, 62, 78, 3, 50, 97, 82, 72]
        pred = bm.get_smallest(random_number_list)
        self.assertEqual(pred, 3)

        random_number_list = [54, 69, 81, 22, 84, 99, 26, 88, 96, 60]
        pred = bm.get_smallest(random_number_list)
        self.assertEqual(pred, 22)

        random_number_list = [98, 6, 57, 4, 37, 96, 63, 53, 42, 88]
        pred = bm.get_smallest(random_number_list)
        self.assertEqual(pred, 4)

        random_number_list = [83, 89, 36, 20, 70, 75, 44, 56, 21, 77]
        pred = bm.get_smallest(random_number_list)
        self.assertEqual(pred, 20)

        random_number_list = [66, 97, 21, 14, 23, 26, 30, 3, 33, 50]
        pred = bm.get_smallest(random_number_list)
        self.assertEqual(pred, 3)

        random_number_list = [11, 62, 18, 36, 95, 65, 26, 52, 90, 16]
        pred = bm.get_smallest(random_number_list)
        self.assertEqual(pred, 11)

        random_number_list = [56, 51, 11, 48, 88, 9, 35, 86, 70, 69]
        pred = bm.get_smallest(random_number_list)
        self.assertEqual(pred, 9)

        random_number_list = [46, 48, 68, 14, 38, 12, 50, 22, 85, 74]
        pred = bm.get_smallest(random_number_list)
        self.assertEqual(pred, 12)

    def test_get_mean(self):
        random_number_list = [72, 51, 10, 48, 58, 62, 92, 90, 11, 16]
        pred = bm.get_mean(random_number_list)
        self.assertEqual(pred, 51.0)

        random_number_list = [54, 56, 30, 12, 58, 25, 17, 48, 80, 23]
        pred = bm.get_mean(random_number_list)
        self.assertEqual(pred, 40.3)

        random_number_list = [55, 93, 22, 67, 98, 11, 5, 68, 57, 89]
        pred = bm.get_mean(random_number_list)
        self.assertEqual(pred, 56.5)

        random_number_list = [7, 67, 6, 53, 62, 93, 56, 81, 9, 80]
        pred = bm.get_mean(random_number_list)
        self.assertEqual(pred, 51.4)

        random_number_list = [2, 41, 31, 63, 22, 99, 76, 55, 56, 50]
        pred = bm.get_mean(random_number_list)
        self.assertEqual(pred, 49.5)

        random_number_list = [69, 13, 80, 78, 64, 58, 30, 45, 97, 77]
        pred = bm.get_mean(random_number_list)
        self.assertEqual(pred, 61.1)

        random_number_list = [19, 2, 20, 5, 69, 56, 46, 16, 76, 93]
        pred = bm.get_mean(random_number_list)
        self.assertEqual(pred, 40.2)

        random_number_list = [25, 86, 89, 82, 71, 52, 64, 38, 77, 56]
        pred = bm.get_mean(random_number_list)
        self.assertEqual(pred, 64.0)

        random_number_list = [36, 40, 1, 72, 99, 29, 95, 33, 56, 15]
        pred = bm.get_mean(random_number_list)
        self.assertEqual(pred, 47.6)

        random_number_list = [68, 92, 2, 69, 54, 51, 12, 67, 88, 82]
        pred = bm.get_mean(random_number_list)
        self.assertEqual(pred, 58.5)

    def test_get_median(self):
        random_number_list = [6, 75, 79, 41, 38, 77, 1, 30, 69, 83]
        pred = bm.get_median(random_number_list)
        self.assertEqual(pred, 55.0)

        random_number_list = [78, 15, 69, 26, 84, 17, 67, 95, 76, 82]
        pred = bm.get_median(random_number_list)
        self.assertEqual(pred, 72.5)

        random_number_list = [79, 86, 48, 45, 68, 4, 73, 84, 31, 98]
        pred = bm.get_median(random_number_list)
        self.assertEqual(pred, 70.5)

        random_number_list = [67, 87, 37, 35, 79, 56, 78, 27, 80, 10]
        pred = bm.get_median(random_number_list)
        self.assertEqual(pred, 61.5)

        random_number_list = [95, 73, 35, 93, 90, 38, 58, 43, 91, 19]
        pred = bm.get_median(random_number_list)
        self.assertEqual(pred, 65.5)

        random_number_list = [6, 93, 23, 7, 3, 99, 36, 51, 70, 89, 5]
        pred = bm.get_median(random_number_list)
        self.assertEqual(pred, 36)

        random_number_list = [99, 13, 18, 41, 32, 44, 85, 24, 23, 27, 21]
        pred = bm.get_median(random_number_list)
        self.assertEqual(pred, 27)

        random_number_list = [82, 64, 49, 47, 78, 35, 26, 87, 8, 29, 97]
        pred = bm.get_median(random_number_list)
        self.assertEqual(pred, 49)

        random_number_list = [28, 74, 4, 24, 91, 21, 27, 38, 70, 95, 35]
        pred = bm.get_median(random_number_list)
        self.assertEqual(pred, 35)

        random_number_list = [33, 24, 23, 92, 30, 40, 38, 95, 87, 69, 68]
        pred = bm.get_median(random_number_list)
        self.assertEqual(pred, 40)
