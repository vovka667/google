#!/usr/bin/python2

import unittest
import solution

class WidgetTestCase(unittest.TestCase):
    def test_google0(self):
        self.assertEqual(solution.solution([2, -3, 1, 0, -5]), 30)

    def test_google1(self):
        self.assertEqual(solution.solution([2, 0, 2, 2, 0]), 8)

    def test_google2(self):
        self.assertEqual(solution.solution([-2, -3, 4, -5]), 60)

    def test_one_positive(self):
        self.assertEqual(solution.solution([2]), 2)

    def test_one_negative(self):
        self.assertEqual(solution.solution([-2]), 0)

    def test_zero(self):
        self.assertEqual(solution.solution([0]), 0)

    def test_zeros(self):
        self.assertEqual(solution.solution([0, 0, 0, 0]), 0)

    def test_one(self):
        self.assertEqual(solution.solution([1]), 1)

    def test_ones(self):
        self.assertEqual(solution.solution([1, 1, 1]), 1)

    def test_minus_ones(self):
        self.assertEqual(solution.solution([-1, -1, -1]), 1)

    def test_various_ones(self):
        self.assertEqual(solution.solution([1, -1]), 1)

    def test_one_negative_one_positive(self):
        self.assertEqual(solution.solution([1, -2]), 1)

    def test_one_negative(self):
        self.assertEqual(solution.solution([-2]), 0)

    def test_one_negative_zero(self):
        self.assertEqual(solution.solution([-2, 0]), 0)

if __name__ == '__main__':
    unittest.main()
