#!/usr/bin/python2

import unittest
import solution

class WidgetTestCase(unittest.TestCase):
    def test_google1(self):
        self.assertEqual(solution.solution([2, 0, 2, 2, 0]), 8)

    def test_google2(self):
        self.assertEqual(solution.solution([-2, -3, 4, -5]), 60)

if __name__ == '__main__':
    unittest.main()
