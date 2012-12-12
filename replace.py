#!/usr/bin/env python
import argparse
import re
import fileinput
from path import path


def load_and_replace(search_re, replace_str, search_path, file_types):
    for sub_file in search_path.walk():
        if sub_file.isfile() and sub_file.ext in file_types or file_types == None:  ## unweildly
            fe = fileinput.FileInput(sub_file,inplace=1)
            for line in fe:
                b = re.sub(search_re,replace_str,line)
                if b != line:
                    print b,
                else:
                    print line,
            fe.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='search replaces based on regex on all files.')
    parser.add_argument('--search', dest='search', help="search regex", type=str, required=True)
    parser.add_argument('--replace',dest='replace', help="replace string", type=str, required=True)
    parser.add_argument('--dir', dest='path', help="what dir to search in", type=path, default=path('.'))
    parser.add_argument('--file_types', dest='types', help="what file types to search", nargs='+',action='store')
    args = parser.parse_args()
    load_and_replace(args.search, args.replace, args.path, args.types)

