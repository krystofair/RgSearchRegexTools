#!/bin/python3

import sys

# function or method invoke
PATTERN = r'\s*(\w+\.)*{func}\('

def format(funcname=r"\w+"):
    return PATTERN.format(func=funcname)

def parse(*args):
    format_names = ['funcname']
    return format(**{format_names[i]: args[i]
                     for i in range(len(args)) if args[i] != '-'})

if __name__ == "__main__":
    try:
        sys.stdout.write(parse(*sys.argv[1:]))
    except:
        sys.exit(-1)
    sys.exit(0)
