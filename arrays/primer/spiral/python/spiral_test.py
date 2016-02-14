#!/usr/bin/env python2

import sys
import unittest as ut

sys.path.append("../../../../tools/python") # I know this is ugly, but whateva!
import json_tools as jt

from spiral import * # This is current directory, not need to add it to the path

class TestSpiral(ut.TestCase):
    def test_json(self):
        # Load the file
        var = jt.json2vars('../spiral.json')
        inp = var['input'] 
        out = var['output']
        print "Check the lengths of the input/output pairs..."
        assert len(inp) == len(out)

        print "Found %d cases, running now..."%len(inp)
        for idx, case in enumerate(inp):
            assert out[idx] == spiralOrder(case)
            print "Case %d done..."%(idx+1)

if __name__ == '__main__':
    ut.main()



