#!/usr/bin/python2

import unittest
import solution

class WidgetTestCase(unittest.TestCase):
    def test_google0(self):
        self.assertEqual(solution.solution('2', '4'), 'impossible')

    def test_google1(self):
        self.assertEqual(solution.solution('2', '1'), '1')

    def test_google2(self):
        self.assertEqual(solution.solution('4', '7'), '4')

if __name__ == '__main__':
    unittest.main()
