import sys, re
from snackpie import SAY, ASk, VAR, prog


def read_file(file):
    with open(file) as f:
        for l in f:
            exexcute(l.strip())

def exexcute(line):
    if not line:
        return
    prog(line)

def main():
    if len(sys.argv) == 2:
        read_file(sys.argv[1])
    else:
        read_file(input('file: '))

if __name__ == '__main__':
    main()