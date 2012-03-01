#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
a surpriser that calls the spain.inquisition.surprise or surprise_file
n times
"""

from spain.inquisition import surprise, surprise_file
import argparse


def main():
    """ parses arguments, calls surprise methods
    """
    parser = argparse.ArgumentParser(
    description="Surprises you in a pythonic way",
    usage="use it like this",
    epilog="Author jsuvileh, demo for t-106.12xx")
    parser.add_argument("-#", "--count", type=int, nargs="?", 
                        default=5, dest="count",
                        help="how many surprises")
    parser.add_argument("-f", "--filename", dest="filename", 
                        default="",
                        help="""file name to write to. implicitly

                        calls surprise_file """)

    args = parser.parse_args()
    for _ in range(args.count):
        if len(args.filename) > 0:
            surprise_file(args.filename)
        else:
            surprise()

    


if __name__ == '__main__':
    main()
