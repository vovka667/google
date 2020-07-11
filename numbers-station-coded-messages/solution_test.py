#!/usr/bin/python2

import unittest
import solution

class WidgetTestCase(unittest.TestCase):
    def test_google1(self):
        self.assertEqual(solution.solution([1, 2, 3, 4], 15), [-1, -1])

    def test_google2(self):
        self.assertEqual(solution.solution([4, 3, 10, 2, 8], 12), [2, 3])

    def test_single1(self):
        self.assertEqual(solution.solution([4, 3, 12, 2, 8], 12), [2, 2])

    def test_single2(self):
        self.assertEqual(solution.solution([4], 4), [0, 0])

if __name__ == '__main__':
    unittest.main()
