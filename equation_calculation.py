

def ask_equation():
    user_input = input("Enter your equation : ")
    #analyze input to separate different types (operators, int and floats)
    i = 0
    element_equation = list(user_input)
    valid_operators = ["+","-","*","/","%","**","//"]
    while i < len(element_equation):
        if "." in element_equation[i] :
            element_equation[i] = float(element_equation[i])
        elif element_equation[i] in valid_operators:
            element_equation[i] = str(element_equation[i])
        else:
            element_equation[i] = int(element_equation[i])
        i+=1
    return tuple(element_equation)

#Function to carry out multiplication
def multiplication(equation):
    equation_list = list(equation)

    while "*" in equation_list:
        position = equation_list.index("*")
        calculation= equation_list[position-1] * equation_list[position+1]
        equation_list[position-1:position+2] = [calculation]
    return tuple(equation_list)

#Function to carry out division
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

#Function to carry out modulus
def modulus(equation):
    equation_list = list(equation)

    while "%" in equation_list:
        position = equation_list.index("%")
        calculation= equation_list[position-1] % equation_list[position+1]
        equation_list[position-1:position+2] = [calculation]
    return tuple(equation_list)

#Function to carry out exponentiation
def exponentiation(equation):
    equation_list = list(equation)

    while "**" in equation:
        position = equation_list.index("**")
        calculation= equation_list[position-1] ** equation_list[position+1]
        equation_list[position-1:position+2] = [calculation]
    return tuple(equation_list)

#Function to carry out floor division
def floor_division(equation):
    equation_list = list(equation)

    while "//" in equation_list:
        position = equation_list.index("//")
        calculation= equation_list[position-1] // equation_list[position+1]
        equation_list[position-1:position+2] = [calculation]
    return tuple(equation_list)

#Function to carry out addition
def addition(equation):
    equation_list = list(equation)
    while "+" in equation_list:
        position = equation_list.index("+")
        calculation = equation_list[position-1] + equation_list[position+1]
        equation_list[position-1:position+2] = [calculation]
    return tuple(equation_list)

#Function to carry out substraction
def substraction(equation):
    equation_list = list(equation)

    while "-" in equation_list:
        position = equation_list.index("-")
        calculation= equation_list[position-1] - equation_list[position+1]
        equation_list[position-1:position+2] = [calculation]
    return tuple(equation_list)

#Function to set calculation priorities      
def priority(equation):
    
    updated_equation = multiplication(equation)
    updated_equation = division(updated_equation)
    updated_equation = modulus(updated_equation)
    updated_equation = exponentiation(updated_equation)
    updated_equation = floor_division(updated_equation)
    updated_equation = addition(updated_equation)
    updated_equation = substraction(updated_equation)

    return updated_equation

#Main program loop
def main():

    user_equation = ask_equation()

    final_result = priority(user_equation)

    print(f"{user_equation} = {final_result}")
    

# the main function 
if __name__ == "__main__":
    main()


