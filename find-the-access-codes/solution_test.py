#!/usr/bin/python2

import unittest
import solution

class WidgetTestCase(unittest.TestCase):
    def test_google0(self):
        self.assertEqual(solution.solution([1, 2, 3, 4, 5, 6]), 3)

    def test_google1(self):
        self.assertEqual(solution.solution([1, 1, 1]), 1)

if __name__ == '__main__':
    unittest.main()
