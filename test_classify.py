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
def inputData(fname):
    pop   = {}
    boundaries = []
    pids  = []
    f = open(fname)
    index = 0
    for line in f:
        
    
        data = line.strip().split()
        this_pop = data[-1]
        this_id  = data[0]
        pids.append(this_id)
        boundaries = list(map(int, sys.argv[2:]))
        if this_pop in pop:
            pop[this_pop].append(index)
        else:
            pop[this_pop]=[index]
        index=index+1
    return boundaries, pop, pids




class TestExclude(unittest.TestCase):

    def setUp(self):
        self.test_data = classify.inputData(os.path.join(this_dir,"data.txt"))
    def test_syntax(self):
        self.assertEqual(classify.fname,sys.argv[0])
        

   
if __name__ == '__main__':


    unittest.main()