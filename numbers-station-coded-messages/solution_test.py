#!/usr/bin/python2

import unittest
import solution

class WidgetTestCase(unittest.TestCase):
    def test_google1(self):
        self.assertEqual(solution.solution([1, 2, 3, 4], 15), [-1, -1])

    def test_google2(self):
        self.assertEqual(solution.solution([4, 3, 10, 2, 8], 12), [2, 3])

    def test_single(self):
        self.assertEqual(solution.solution([4, 3, 12, 2, 8], 12), [2, 2])

    def test_single2(self):
        self.assertEqual(solution.solution([4], 4), [0, 0])

    def test_single2(self):
        self.assertEqual(solution.solution([4, 13, 12, 2, 8], 12), [2, 2])

    def test_single3(self):
        self.assertEqual(solution.solution([13], 12), [-1, -1])

    def test_single4(self):
        self.assertEqual(solution.solution([4, 13, 12, 2, 8], 12), [2, 2])

    def test_single5(self):
        self.assertEqual(solution.solution([12], 13), [-1, -1])

    def test_single6(self):
        self.assertEqual(solution.solution([4, 13, 12, 2, 8], 8), [4, 4])

    def test_single7(self):
        self.assertEqual(solution.solution([4, 13, 12, 2, 8], 4), [0, 0])

    def test_single7(self):
        self.assertEqual(solution.solution([43, 13, 12, 2, 8], 8), [4, 4])

if __name__ == '__main__':
    unittest.main()
