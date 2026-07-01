import sys, re
from snackpie import prog, IFstatement


def read_file(file):
    with open(file) as f:
        lines = f.readlines()

    i = 0

    while i < len(lines):

        line = lines[i].rstrip('\n')

        if line.startswith('if '):

            obj = IFstatement()

            bodies = {}

            cond = line[3:-1].strip()

            bodies[cond] = []

            current_cond = cond

            i += 1

            while i < len(lines):

                com = lines[i].rstrip('\n')

                if com == 'end':
                    break

                elif com.startswith('orif '):

                    current_cond = com[5:-1].strip()

                    bodies[current_cond] = []

                elif com == 'else:':

                    current_cond = 'else'

                    bodies[current_cond] = []

                elif com.startswith(' '):

                    bodies[current_cond].append(
                        com.strip()
                    )

                i += 1

            for condition, body in bodies.items():
                obj.add_branch(condition, body)

            obj.evaluate()

        else:
            exexcute(line)

        i += 1
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