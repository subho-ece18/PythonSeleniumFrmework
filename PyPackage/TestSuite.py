from unittest.suite import TestSuite
__author__ = 'rahul'
 
import unittest
from PyPackage import GooglePage
from PyPackage import MyWikiTestCases
import os
#from PyPackage import html-testRunner
from PyPackage import HTMLTestRunner
 
direct = os.getcwd()
 
class MyTestSuite(unittest.TestCase):
 
    def test_Issue(self):
 
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(MyWikiTestCases.MyWikiTestCase),
            unittest.defaultTestLoader.loadTestsFromTestCase(GooglePage.MyGoogleTest),
        ])
 
        outfile = open(direct + "\SmokeTest.html", "w")
 
        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Test Report',
            description='Smoke Tests'
        )
 
        runner1.run(smoke_test)
 
 
 
 
 
if __name__ == '__main__':
    unittest.main()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestSuite)
    unittest.TextTestRunner().run(suite)
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))