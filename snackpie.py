# variable = {}
# v_mark="="
# print_code="say"
# input_code="ask"

# while True:
#     code=input("").split(' ')
    
    

# #this function for print 
#     def print_s():
#         try:
#             if variable[code[1]]:
#                 print('>>>>'+variable[code[1]])
#         except:
#             print(">>>>"+code[1]) 
    
    

# #this function for input
#     def input_s():
#         if not('=' in code):
#             input(">>>>" +code[1] +" ")
#         elif '=' in code:
#             value = input('>>>>'+code[3]+' ')
#             variable[code[0]] = value
    
    

# #this function for variables
#     def variables(code):
#             if len(code) > 1:
#                 variable[code[0]] = code[2]
#             elif len(code) == 1:
#                 code = code[0].split('=')
#                 variable[code[0]] = code[1]         


#     if print_code in code:
#         print_s()
#     elif input_code in code:
#         input_s()
#     elif v_mark in code:
#         variables(code)


#============================================
import sys, re

class SAY:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        t = VAR().ver_type(str(self.value))
        if VAR().is_v(self.value):
            return f'>>>>{VAR().get_v(self.value)['value']}'
        return f'>>>>{self.value}' if t not in ['intger', 'float'] else f'>>>>{self.value}'

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if not value:
            raise ValueError("There is no value")
        self._value = value

class ASk:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'>>>>{self.value}'

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if not value:
            raise ValueError("There is no value")
        self._value = input(value)

class VAR:
    all = {}
    def __init__(self, name=None, value=None):
        self.add_v(name, value)
    
    @classmethod
    def add_v(cls, n:str, v) -> bool:
        if not n or not v:
            pass
        else:
            from_ask = False
            if 'ask' in v:
                inp = list(map(str.lstrip, v.split('ask')))
                v = ASk(inp[-1]).value
                from_ask = True
            if VAR().is_v(n):
                if n.startswith('_'):
                    print('ERROR: This is a const, it can\'t be changed')
                    print('INFO: Type "HINT" to show the instructions')
                    return
                else:
                    print(f'The old value is {VAR().get_v(n)['value']}')
            is_quoted = (v.startswith("'") and v.endswith("'")) or (v.startswith('"') and v.endswith('"'))
            if is_quoted:
                v = v[1:-1]
            else:
                gu_re = re.findall(r"\d+(?:\.\d+)?|[+\-*/]", v)
                if gu_re:
                    v = str(calc(gu_re))
                elif not from_ask and not VAR().is_v(v):
                    raise TypeError("ERROR: I think that you're missing \" or ' :>")
            
            t = cls.ver_type(v)
            if t == 'intger':
                v= int(float(v))
            elif t == 'float':
                v = float(v)
            else:
                v =str(v)
            cls.all[n] = None
            cls.all[n] = {
                "value":v,
                "type": t
            }
            return True
    
    @staticmethod
    def ver_type(var):
        var = var.removesuffix('.0')
        if var.isdigit():
            return 'intger'
        
        try:
            var = float(var)
        except Exception:
            return 'string'
        else:
            return 'float'
    
    @classmethod
    def get_v(cls, n:str):
        if not n:
            raise ValueError
        return cls.all[n]
    
    @classmethod
    def is_v(cls, n:str) -> bool:
        if not n:
            raise ValueError
        return n in cls.all.keys()

class IFstatement:
    def __init__(self):
        self.branches = []

    # body = list of commands
    def add_branch(self, condition, body):
        self.branches.append((condition, body))

    def parse_value(self, value):
        value = value.strip()

        if (
            (value.startswith("'") and value.endswith("'"))
            or
            (value.startswith('"') and value.endswith('"'))
        ):
            return value[1:-1]

        if VAR.is_v(value):
            value = VAR.get_v(value)["value"]

        try:
            return int(value)
        except:
            pass

        try:
            return float(value)
        except:
            pass

        return value

    def evaluate(self):
        else_body = None
        
        for condition, body in self.branches:

            if condition == "else":
                else_body = body
                continue

            cond_re = re.match(
                r"(.+?)\s*(>=|<=|==|!=|>|<)\s*(.+)",
                condition
            )

            if not cond_re:
                raise SyntaxError(
                    f"Invalid condition: {condition}"
                )

            left = cond_re.group(1).strip()
            op = cond_re.group(2).strip()
            right = cond_re.group(3).strip()

            left = self.parse_value(left)
            right = self.parse_value(right)

            state = False
            print(left, op, right)
            if op == ">":
                state = left > right

            elif op == "<":
                state = left < right

            elif op == ">=":
                state = left >= right

            elif op == "<=":
                state = left <= right

            elif op == "==":
                state = left == right

            elif op == "!=":
                state = left != right

            if state:
                self.execute(body)
                return

        if else_body is not None:
            self.execute(else_body)

    def execute(self, body):
        print(body)
        for command in body:
            prog(command, True)

def calc(exp):
    gu_re = exp  #1*2*3*4*5*6/456*90
    sums = 0
    new_gu = gu_re.copy()
    while '*' in new_gu or '/' in new_gu:
        try:
            cr=new_gu.index('*') if '*' in new_gu else None
            dv=new_gu.index('/') if '/' in new_gu else None
            if cr or dv:
                if (cr and not dv) or (cr and dv and cr<dv):
                    lst = float(new_gu[cr-1])
                    nxt = float(new_gu[cr+1])
                    m = lst * nxt
                    new_gu[cr] = m
                    new_gu.pop(cr+1)
                    new_gu.pop(cr-1)
                elif (dv and not cr) or (cr and dv and cr>dv):
                    lst = float(new_gu[dv-1])
                    nxt = float(new_gu[dv+1])
                    m = lst / nxt
                    new_gu[dv] = m
                    new_gu.pop(dv+1)
                    new_gu.pop(dv-1)
        except IndexError:
            break
    while '+' in new_gu or '-' in new_gu:
        try:
            pl=new_gu.index('+') if '+' in new_gu else None
            mi=new_gu.index('-') if '-' in new_gu else None
            if pl or mi:
                if (pl and not mi) or (pl and mi and pl<mi):
                    lst = float(new_gu[pl-1])
                    nxt = float(new_gu[pl+1])
                    m = lst + nxt
                    new_gu[pl] = m
                    new_gu.pop(pl+1)
                    new_gu.pop(pl-1)
                elif (mi and not pl) or (pl and mi and pl>mi):
                    lst = float(new_gu[mi-1])
                    nxt = float(new_gu[mi+1])
                    m = lst - nxt
                    new_gu[mi] = m
                    new_gu.pop(mi+1)
                    new_gu.pop(mi-1)
        except IndexError:
            break
    else:
        return new_gu[0]

def prog(com, ig=False):
    try:
        command = com

        say_re = re.search(r"^say (?:(\".+\")|(\'.+\')|(.+))$", command)
        ask_re = re.search(r"^ask (?:(\".+\")|(\'.+\')|(.+))$", command)
        var_re = re.search(r"^([^=]+) ?= ?(ask )?(?:(\".+?\")|(\'.+?\')|(.+))$", command)
        gu_re = re.findall(r"\d+(?:\.\d+)?|[+\-*/]", command)

        if not command:
            raise ValueError('Invalid syntax')
        
        if command.startswith('if ') and ig == False:
            obj = IFstatement()
            bodies = {}
            cond = command[3:-1]
            bodies[cond] = None
            commands = []
            com = ''
            while com != 'end':
                com = input('....')
                if 'orif' in com:
                    commands = []
                    cond = com[5:-1]
                    bodies[cond] = None
                elif 'else' in com:
                    commands = []
                    cond = 'else'
                    bodies[cond] = None
                elif com[0] == ' ':
                    commands.append(com[1:])
                    bodies[cond] = commands
            for condition in bodies:
                obj.add_branch(condition, bodies[condition])
            obj.evaluate()
        elif say_re:
            if "\"" in command:
                rel_v = say_re.group(1)[1:-1]
            elif "'" in command:
                rel_v = say_re.group(2)[1:-1]
            elif say_re.group(3):
                rel_v = say_re.group(3)
            else:
                rel_v = ""
            print(SAY(rel_v))
        elif var_re:
            if var_re.group(3):
                rel_v = var_re.group(3)
            elif var_re.group(4):
                rel_v = var_re.group(4)
            else:
                rel_v = var_re.group(5)
            ins_vars = VAR(var_re.group(1).strip(), var_re.group(2)+rel_v if var_re.group(2) else rel_v)
        elif ask_re:
            if "\"" in command:
                rel_v = ask_re.group(1)
            elif "'" in command:
                rel_v = ask_re.group(2)
            else:
                ty = VAR().ver_type(ask_re.group(3))
                if ty == 'string' and not VAR().is_v(ask_re.group(3)):
                    raise TypeError("ERROR: I think that you're missing \" or ' :>")
                rel_v = ask_re.group(3)
            print(ASk(rel_v))
        elif gu_re:
            print(SAY(calc(gu_re)))
        elif command == 'exit()':
            raise EOFError
        else:
            raise TypeError("ERROR: I think that you're missing \" or ' :>")
    except EOFError:
        sys.exit('OUT')
    except Exception as e:
        sys.exit(str(e))


def main():
    if len(sys.argv) == 2:
        # read file directly
        with open(sys.argv[1]) as f:
            lines = f.readlines()
        for line in lines:
            prog(line.rstrip('\n'))
    else:
        while True:
            try:
                prog(input(""))
            except EOFError:
                sys.exit('OUT')

if __name__ == '__main__':
    main()
