'''
Created on Mar 28, 2019

@author: PC
'''
import unittest
import xmlrunner

class TestCalc(unittest.TestCase):

    def testAdd(self):
        print("it is a test")
        result = True
        self.assertEqual(result, True, "Ohno")
if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='C:\\Users\\PC\\eclipse-workspace\\TestPython\\test_report'),
        # these make sure that some options that are not applicable
        # remain hidden from the help menu.
        failfast=False, buffer=False, catchbreak=False)
    