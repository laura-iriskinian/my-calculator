
def ask_equation():
    element_equation = []
    valid_operators = ["+","-","*","/","%","**","//"]
    while True :
        user_input = input("Enter number or operator : ")
        if user_input.lower() == "q":
            break
        elif user_input in valid_operators:
            element_equation.append(str(user_input))  
        elif "." in user_input:
            element_equation.append(float(user_input))
        else:
            element_equation.append(int(user_input))    
    return tuple(element_equation)


def multiplication(equation):
    equation_list = list(equation)

    while "*" in equation_list:
        position = equation_list.index("*")
        calculation= equation_list[position-1] * equation_list[position+1]
        equation_list[position-1:position+2] = [calculation]
    return tuple(equation_list)


def division(equation):
    equation_list = list(equation)
    try:
        while "/" in equation_list:
            position = equation_list.index("/")
            calculation= equation_list[position-1] / equation_list[position+1]
            equation_list[position-1:position+2] = [calculation] 
        return tuple(equation_list)
    except ZeroDivisionError:
        print("division par zéro impossible")
        return equation_list

def modulus(equation):
    equation_list = list(equation)

    while "%" in equation_list:
        position = equation_list.index("%")
        calculation= equation_list[position-1] % equation_list[position+1]
        equation_list[position-1:position+2] = [calculation]
    return tuple(equation_list)

def exponentiation(equation):
    equation_list = list(equation)

    while "**" in equation:
        position = equation_list.index("**")
        calculation= equation_list[position-1] ** equation_list[position+1]
        equation_list[position-1:position+2] = [calculation]
    return tuple(equation_list)

def floor_division(equation):
    equation_list = list(equation)

    while "//" in equation_list:
        position = equation_list.index("//")
        calculation= equation_list[position-1] // equation_list[position+1]
        equation_list[position-1:position+2] = [calculation]
    return tuple(equation_list)

def addition(equation):
    equation_list = list(equation)
    while "+" in equation_list:
        position = equation_list.index("+")
        calculation = equation_list[position-1] + equation_list[position+1]
        equation_list[position-1:position+2] = [calculation]
    return tuple(equation_list)

def substraction(equation):
    equation_list = list(equation)

    while "-" in equation_list:
        position = equation_list.index("-")
        calculation= equation_list[position-1] - equation_list[position+1]
        equation_list[position-1:position+2] = [calculation]
    return tuple(equation_list)
        
def priority(equation):
    
    updated_equation = multiplication(equation)
    updated_equation = division(updated_equation)
    updated_equation = modulus(updated_equation)
    updated_equation = exponentiation(updated_equation)
    updated_equation = floor_division(updated_equation)
    updated_equation = addition(updated_equation)
    updated_equation = substraction(updated_equation)

    return updated_equation

def main():

    user_equation = ask_equation()

    final_result = priority(user_equation)

    print(f"{user_equation} = {final_result}")
    

# the main def 
if __name__ == "__main__":
    main()


