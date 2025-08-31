#!/bin/python3

import sys


PATTERN = (r'(?:from\s+[\.\w]*{module}(\.\w+)*\s+import\s+({func})'
           r'|import\s+{module}\.?{func})')

def format(modname=r"[\w\.]+", funcname=r"\w*"):
    return PATTERN.format(module=modname, func=funcname)

def parse(*args):
    format_names = ['modname', 'funcname']
    return format(**{format_names[i]: args[i]
                     for i in range(len(args)) if args[i] != '-'})

if __name__ == "__main__":
    try:
        sys.stdout.write(parse(*sys.argv[1:]))
    except:
        sys.exit(-1)
    sys.exit(0)
