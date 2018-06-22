#!/usr/bin/env python

import sys
sys.path.insert(0, '..')

import numpy

from utils.io import array2root
from root_numpy import root2array

# folding_weights.dtype = [('weight', numpy.float64)]
test_array = numpy.array([(1, 2.5, 3.4), (4, 5, 6.8)],
                        dtype=[('a', int), ('b', float), ('c', float)])

# Write the new weights to a root tree
array2root(test_array, 'test_tree.root', 'test_tree', mode='recreate')

# Now read from the newly-created root file, and compare
test_array_read = root2array('test_tree.root', 'test_tree',
                             branches=['a', 'b', 'c'])
print('Test if two arrays equal: %s' %
      numpy.array_equal(test_array, test_array_read))
