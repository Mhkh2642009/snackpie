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
        if VAR().is_v(self.value):
            return f'>>>>"{VAR().get_v(self.value)}"'
        return f'>>>>"{self.value}"'

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
                inp = list(map(str.strip, v.split('ask')))
                v = ASk(inp[-1]).value
            if VAR().is_v(n):
                if n.startswith('_'):
                    print('ERROR: This is a const, it can\'t be changed')
                    print('INFO: Type "HINT" to show the instructions')
                    return
                else:
                    print(f'The old value is {VAR().get_v(n)}')
            cls.all[n] = v
            return True 
    
    @classmethod
    def get_v(cls, n:str):
        if not n:
            raise ValueError
        return cls.all[n]
    
    @classmethod
    def is_v(cls, n:str) -> bool:
        if not n:
            raise ValueError
        return True if n in cls.all.keys() else False
    
    

try:
    while True:
        
        command = input("")

        say_re = re.search(r"^say (?:\"(.+)\"|\'(.+)\')$", command)
        ask_re = re.search(r"^ask (?:\"(.+)\"|\'(.+)\')$", command)
        var_re = re.search(r"^(.+) ?= ?(?:\"([a-zA-Z0-9]+)\"|\'([a-zA-Z0-9]+)\')$", command)

        if not command:
            raise ValueError('Invalid syntax')
        
        if say_re:
            rel_v = say_re.group(1) if "\"" in command else say_re.group(2)
            print(SAY(rel_v))
        elif var_re:
            rel_v = var_re.group(2) if "\"" in command else var_re.group(3)
            ins_vars = VAR(var_re.group(1), rel_v)
        elif ask_re:
            rel_v = ask_re.group(1) if "\"" in command else ask_re.group(2)
            print(ASk(rel_v))
        elif command == 'exit()':
            raise EOFError
        else:
            raise TypeError("ERROR: I think that you're missing \" or ' :>")
except EOFError:
    sys.exit('OUT')
except Exception as e:
    sys.exit(str(e))