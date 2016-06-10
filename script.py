
#!/usr/bin/env python

"""
	wena compare
"""

import os
import sys
import argparse
import json


def main(arguments):

    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('infile_2015', help="Input file 2015", type=argparse.FileType('r'))
    parser.add_argument('infile_2016', help="Input file 2016", type=argparse.FileType('r'))
    parser.add_argument('-o', '--outfile', help="Output file", default=sys.stdout, type=argparse.FileType('w'))

    args = parser.parse_args(arguments)
    data_2015 = json.load(args.infile_2015)
    data_2016 = json.load(args.infile_2016)

    print len(data_2015)
    print len(data_2016)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))