import sys, re
from snackpie import SAY, ASk, VAR


def read_file(file):
    with open(file) as f:
        for l in f:
            exexcute(l.strip())

def exexcute(line):
    if not line:
        return
    try:
        command = line

        say_re = re.search(r"^say (?:\"(.+)\"|\'(.+)\'|(.+))$", command)
        ask_re = re.search(r"^ask (?:\"(.+)\"|\'(.+)\')$", command)
        var_re = re.search(r"^(.+) ?= ?(ask )?(?:\"(.+)\"|\'(.+)\')$", command)
        gu_re = re.search(r"^([0-9]\.?[0-9]*) ?(\+|\-|\*|\/) ?([0-9]\.?[0-9]*)$", command.strip())

        if not command:
            raise ValueError('Invalid syntax')
        
        if say_re:
            if "\"" in command:
                rel_v = say_re.group(1)
            elif "'" in command:
                rel_v = say_re.group(2)
            else:
                rel_v = say_re.group(3)
            print(SAY(rel_v))
        elif var_re:
            rel_v = var_re.group(3) if var_re.group(3) else var_re.group(4)
            ins_vars = VAR(var_re.group(1).strip(), var_re.group(2)+rel_v if var_re.group(2) else rel_v)
        elif ask_re:
            rel_v = ask_re.group(1) if "\"" in command else ask_re.group(2)
            print(ASk(rel_v))
        elif gu_re:
            f_n = [gu_re.group(1), VAR().ver_type(gu_re.group(1))]
            s_n = [gu_re.group(3), VAR().ver_type(gu_re.group(3))]
            op = gu_re.group(2)
            if f_n[1] != s_n[1]:
                raise ValueError('Not same data types')
            if f_n[1] == 'string':
                raise ValueError('Can\'t do that')
            if f_n[-1] == 'intger':
                f_n= int(f_n[0])
            else:
                f_n= float(f_n[0])
            if s_n[-1] == 'intger':
                s_n= int(s_n[0])
            else:
                s_n= float(s_n[0])
            
            if op == '+':
                res = f_n+s_n
            elif op == '-':
                res = f_n-s_n
            elif op == '*':
                res = f_n*s_n
            else:
                res = f_n/s_n
            print(SAY(res))
        elif command == 'exit()':
            raise EOFError
        else:
            raise TypeError("ERROR: I think that you're missing \" or ' :>")
    except EOFError:
        sys.exit('OUT')
    except Exception as e:
        sys.exit(str(e))

def main():
    read_file(input('file: '))

if __name__ == '__main__':
    main()