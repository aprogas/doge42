#!/usr/bin/env python
# 
# Copyright (C) 2013 Jasper Jongmans
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE. 
# 

import sys
import argparse

def calc_cost(distance, relation):
    '''Calculates trade post cost, expects distance as fractional multiplier'''
    return 150 * distance * (1 - 0.004*relation)

def relation_bribed(relation_current, bribe_effect):
    '''Returns new relation maximised at 100, expects whole numbers'''
    return min(100, relation_current + bribe_effect)

if __name__ == '__main__':
    # Define command-line options
    parser = argparse.ArgumentParser(description='Calculate effectiveness of bribing top liege before building tradeposts.')
    parser.add_argument('-d', '--distance', type=float, default=0)
    parser.add_argument('-r', '--relation', type=int, default=0)
    parser.add_argument('-b', '--bribe-cost', type=float, default=0)
    parser.add_argument('-e', '--bribe-effect', type=int, default=0)
    # Read options and normalise
    args = parser.parse_args()
    distance_mult = 1 + args.distance / 100.0
    
    # Calculate both scenarios
    cost1 = calc_cost(distance_mult, args.relation)
    print "Cost per tradepost without bribe : {:7.2f}".format(cost1)
    if args.bribe_effect:
        cost2 = calc_cost(distance_mult, relation_bribed(args.relation, args.bribe_effect))
        breakeven = args.bribe_cost / (cost1 - cost2)
        print "Cost per tradepost with bribe    : {:7.2f}".format(cost2)
        print "Cost for 1 tradepost and bribe   : {:7.2f}".format(cost2 + args.bribe_cost)
        print "Tradeposts needed to break even  : {: .2f}".format(breakeven)
