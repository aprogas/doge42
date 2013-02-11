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
from optparse import OptionParser

def calc_cost(distance, relation):
    '''Calculates trade post cost, expects distance as fractional multiplier'''
    return 150 * distance * (1 - 0.004*relation)

def relation_bribed(relation_current, bribe_effect):
    '''Returns new relation maximised at 100, expects whole numbers'''
    return min(100, relation_current + bribe_effect)

if __name__ == '__main__':
    # Define command-line options
    parser = OptionParser()
    parser.add_option('-d', '--distance', action='store', dest='distance')
    parser.add_option('-r', '--relation', action='store', dest='relation')
    parser.add_option('-b', '--bribe-cost', action='store', dest='bribe_cost', default=0)
    parser.add_option('-e', '--bribe-effect', action='store', dest='bribe_effect', default=0)
    # Read options, check sanity, and normalise
    (options, args) = parser.parse_args()
    try:
        distance = 1 + float(options.distance) / 100.0
    except:
        parser.error('Could not parse distance, enter as in game but without + or %, e.g. 102.4')
    try:
        relation = float(options.relation)
    except:
        parser.error('Could not parse relation, enter as whole number, e.g. -23')
    try:
        bribe_cost = float(options.bribe_cost)
    except:
        parser.error('Could not parse bribe cost, enter as shown in game, e.g. 133.7')
    try:
        bribe_effect = int(options.bribe_effect)
    except:
        parser.error('Could not parse bribe effect, enter as whole number, e.g. 42')
    
    # Calculate both scenarios
    cost1 = calc_cost(distance, relation)
    cost2 = calc_cost(distance, relation_bribed(relation, bribe_effect))
    breakeven = bribe_cost / (cost1 - cost2)
    print "Cost per tradepost without bribe : {:7.2f}".format(cost1)
    print "Cost per tradepost with bribe    : {:7.2f}".format(cost2)
    print "Cost for 1 tradepost and bribe   : {:7.2f}".format(cost2 + bribe_cost)
    print "Tradeposts needed to break even  : {: .2f}".format(breakeven)
