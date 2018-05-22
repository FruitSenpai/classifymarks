# -*- coding: utf-8 -*-
"""
Created on Tue May 22 11:05:23 2018

@author: harvey
"""

import unittest
import classify
import os
import sys

this_dir = os.path.dirname(__file__)


class TestExclude(unittest.TestCase):

    def setUp(self):
        self.test_data = classify.inputData(os.path.join(this_dir,"data.txt"))
    def test_syntax(self):
        self.assertEqual(classify.fname,sys.argv[0])
        

   
if __name__ == '__main__':


    unittest.main()