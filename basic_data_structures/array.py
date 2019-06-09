import array
import os
import sys

sys.path.append(os.getcwd())


class Array(object):
    """
    A simple array class template.
    """
    def __init__(self, ndim=1, mdim=1):
        """
        The array template could be a single vector array or a N * M array. Internally the structure is a list of lists, except that the length is fixed.

        :param ndim: Row dimension of the array. Default set to 1.
        :param mdim: Column dimension of the array. Default set to 1.
        """
        self.ndim = ndim
        self.mdim = mdim
        
    def check_length(self):
        pass
    