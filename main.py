""" This is the main file which will be called to execute any data structure or algorithm implemented. """

import argparse
import os
import sys

sys.path.append(os.getcwd())


def arg_parser(system_arguments):
    arguments = list()
    return arguments


if __name__ == '__main__':
    if len(arg_parser(sys.argv)) > 0:
        arguments_passed = arg_parser(sys.argv[1:])
