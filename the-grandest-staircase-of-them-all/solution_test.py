#!/usr/bin/python2

import unittest
import solution

class WidgetTestCase(unittest.TestCase):
    def test_google0(self):
        self.assertEqual(solution.solution(3), 1)

    def test_google1(self):
        self.assertEqual(solution.solution(4), 1)

    def test_google2(self):
        self.assertEqual(solution.solution(5), 2)

    def test_google3(self):
        self.assertEqual(solution.solution(6), 3)

    def test_google4(self):
        self.assertEqual(solution.solution(7), 4)

    def test_google5(self):
        self.assertEqual(solution.solution(8), 5)

    def test_google6(self):
        self.assertEqual(solution.solution(9), 7)

    def test_google7(self):
        self.assertEqual(solution.solution(200), 487067745)

if __name__ == '__main__':
    unittest.main()
