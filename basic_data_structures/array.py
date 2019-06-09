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
        The array template could be a single vector array or a N * M array.
        Internally the structure is a list of lists, except that the length is
        fixed.

        :param ndim: Row dimension of the array. Default set to 1.
        :param mdim: Column dimension of the array. Default set to 1.
        """
        self.ndim = ndim
        self.mdim = mdim
        self.length = (self.ndim, self.mdim)
        self.element_count = self.ndim * self.mdim

    def __check_length(self):
        pass

    def add_element(self, e):
        pass

    def remove_element(self, a):
        pass

    def length(self):
        """ Returns the length of the array. """
        return self.length

    def sum(self):
        pass

    def mean(self):
        pass

    def std_dev(self):
        pass
