import math


def typed_input(prompt:str='', force_type:type=str, error_message:str='', escape_code:str='exit'):
    user_input = input(prompt)
    try:
        user_input = force_type(user_input)
    except ValueError:
        if user_input.upper() == escape_code.upper(): return None 
        else: 
            if error_message != '': print(error_message)
            user_input = typed_input(prompt, force_type, error_message, escape_code)
    finally: return user_input

def get_solution_1(a,b,c):
    try:
        try: return str(-b + math.sqrt((math.pow(b, 2)) - (4*a*c))) / (2*a)
        except ValueError: return str("x = " + str(-b / (2*a)) + " + " + str((math.sqrt(abs((math.pow(b, 2)) - (4*a*c))) / (2*a))) + "i")
    except: return 'None'

def get_solution_2(a,b,c):
    try:
        try: return str(-b - math.sqrt((math.pow(b, 2)) - (4*a*c))) / (2*a)
        except ValueError: return str("x = " + str(-b / (2*a)) + " + " + str(-(math.sqrt(abs((math.pow(b, 2)) - (4*a*c))) / (2*a))) + "i")
    except: return 'None'

def qf(a, b, c):
    print(" ")
    print("Solutions:")
    try: general_solution = str("x = " + str(-b) + " -+ " + "sqrt(" + str(math.pow(b, 2) - (4*a*c)) + ") / " + str(2*a))
    except: return 'No Solutions'
    solution_1 = get_solution_1(a,b,c)
    solution_2 = get_solution_2(a,b,c)

    print(general_solution)
    print('>>>')
    print(solution_1)
    print('or')
    print(solution_2)

    if typed_input('Press enter to exit or input "1" to run again: ', str) == '1': run()
    else: return general_solution, solution_1, solution_2


def run():
    a = typed_input('Input: ', float, error_message='Error: Input must be Integer or Float')
    b = typed_input('Input: ', float, error_message='Error: Input must be Integer or Float')
    c = typed_input('Input: ', float, error_message='Error: Input must be Integer or Float')
    qf(a,b,c)

run()
