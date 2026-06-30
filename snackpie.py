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
            return f'>>>>"{VAR().get_v(self.value)['value']}"'
        return f'>>>>"{self.value}"' if t not in ['intger', 'float'] else f'>>>>{self.value}'

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
            if 'ask' in v:
                inp = list(map(str.lstrip, v.split('ask')))
                v = ASk(inp[-1]).value
            if VAR().is_v(n):
                if n.startswith('_'):
                    print('ERROR: This is a const, it can\'t be changed')
                    print('INFO: Type "HINT" to show the instructions')
                    return
                else:
                    print(f'The old value is {VAR().get_v(n)['value']}')
            t = cls.ver_type(v)
            if t == 'intger':
                v= int(v)
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
        for command in body:
            execute_command(command)


def execute_command(command):
    try:
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
        else:
            raise TypeError("ERROR: I think that you're missing \" or ' :>")
    except Exception as e:
        main()

# need if-statement error handler    
def main():
    try:
        while True:
            
            command = input("")

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
            elif command.startswith('if '):
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
            elif command == 'exit()':
                raise EOFError
            else:
                raise TypeError("ERROR: I think that you're missing \" or ' :>")
    except EOFError:
        sys.exit('OUT')
    except Exception as e:
        sys.exit(str(e))


if __name__ == '__main__':
    main()