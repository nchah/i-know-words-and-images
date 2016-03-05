#!/usr/bin/env python
"""
Wanted a script to pretty print JSON to the command line.

"""

import argparse
import json

__author__ = "NC"


def main(input_file):
    with open(input_file) as f:
        p = json.load(f)
        pp = json.dumps(p, indent=3, sort_keys=True)
        print pp
        # return pp

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='The json file you\'d like to pretty print.')
    args = parser.parse_args()
    main(args.input_file)