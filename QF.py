import math


def QF():
    print(" ")
    print("Equation Form: ax^2 + bx + c = 0")
    print('Input Constants a, b, and c to execute. Input "stop" to terminate program.')
    print(" ")
    while True:
        try:
            a = input("Constant 1 (a): ")
            if a.upper() == "STOP":
                print("Terminating Program...")
                exit()
            elif a.upper() == "HELP":
                print("Error: No Help Avaliable")
            elif a.upper() == "I LOVE MATHS":
                print("Error: Incomprehensible")
            else:
                a = float(a)
                break
        except ValueError:
            print("Error: Input Integer or Float")
    while True:
        try:
            b = input("Constant 2 (b): ")
            if b.upper() == "STOP":
                print("Terminating Program...")
                exit()
            else:
                b = float(b)
                break
        except ValueError:
            print("Error: Input Integer or Float")
    while True:
        try:
            c = input("Constant 3 (c): ")
            if c.upper() == "STOP":
                print("Terminating Program...")
                exit()
            else:
                c = float(c)
                break
        except ValueError:
            print("Error: Input Integer or Float")

    print(" ")
    print("Solutions:")
    try:
        print("x = " + str(-b) + " -+ " + "sqrt(" +
              str(math.pow(b, 2) - (4*a*c)) + ") / " + str(2*a))
    except:
        pass
    try:
        try:
            output_1 = (-b + math.sqrt((math.pow(b, 2)) - (4*a*c))) / (2*a)
            print("x = " + str(output_1))
        except ValueError:
            output_1 = (math.sqrt(abs((math.pow(b, 2)) - (4*a*c))) / (2*a))
            print("x = " + str(-b / (2*a)) + " + " + str(output_1) + "i")
    except:
        output_1 = "None"
        print(output_1)

    if output_1 != "None":
        print("or")

    try:
        try:
            output_2 = (-b - math.sqrt((math.pow(b, 2)) - (4*a*c))) / (2*a)
            print("x = " + str(output_2))
        except ValueError:
            output_2 = -(math.sqrt(abs((math.pow(b, 2)) - (4*a*c))) / (2*a))
            print("x = " + str(-b / (2*a)) + " + " + str(output_2) + "i")
    except:
        output_2 = "None"
        print(output_2)


QF()
