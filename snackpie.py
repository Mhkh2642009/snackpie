variable = {}
v_mark="="
print_code="say"
input_code="ask"

while True:
    code=input("").split(' ')
    
    
#this function for print 
    def print_s():
        try:
            if variable[code[1]]:
                print('>>>>'+variable[code[1]])
        except:
            print(">>>>"+code[1]) 
    
    
#this function for input
    def input_s():
        if not('=' in code):
            input(">>>>" +code[1] +" ")
        elif '=' in code:
            value = input('>>>>'+code[3]+' ')
            variable[code[0]] = value
    
    
#this function for variables
    def variables(code):
            if len(code) > 1:
                variable[code[0]] = code[2]
            elif len(code) == 1:
                code = code[0].split('=')
                variable[code[0]] = code[1]         


    if print_code in code:
        print_s()
    elif input_code in code:
        input_s()
    elif v_mark in code:
        variables(code)