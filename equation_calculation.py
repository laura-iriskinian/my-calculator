import json

#Set a function to create json file to save history
def create_history():
    try:
        with open("history.json","x") as file:
            json.dump({}, file)
    except FileExistsError:
        pass

#Menu function to get user choice
def menu():
    print ("\n\033[0m1. Use the calculator\n2. View history \n3. Delete history \n4. Exit the program")
    
    return input("\nYour choice (1-4) : ")

#Allow recognition of numbers in input string
def search_number():
    create_number = 0
    list_number = []
    while create_number <= 10000:
        list_number.append(str(create_number))
        create_number+=1
    return list_number

#Merge the different parts of the input to carry out valid operations
def concat(element_equation,valid_operators):
    index_operator = []
    index_equation = []
    expo_floor_operators = ["*","/"]
    n = 0
    try:
        while n < len(element_equation):

            # loop to create list with operator index 
            for index, equation in enumerate(element_equation):
                if equation in valid_operators:
                    index_operator.append(index)

            # loop to create list with equation index 
            for ind, equation in enumerate(element_equation):
                index_equation.append(ind)
            
            if len(index_operator) == 0:
                print("\033[1;31mNot operator in equation, enter a valid equation.\033[0m")
                return main()
            
            else:
                start_index_operator = index_operator[n]
                
                
                dif_last_index_equation = index_equation[-1] - index_operator[-1]

                # elif to first numbers (2 2 + ...)
                if start_index_operator >= 2 and n == 0:

                    group_elements = "".join(element_equation[0 :start_index_operator])
                    element_equation[0:start_index_operator] = [group_elements]
                    index_operator[:] = []  
                    index_equation[:] = []
                    n -= 1

                # elif to last number (... + 2 2)
                elif dif_last_index_equation >= 2 and n == 0:

                    group_elements = "".join(element_equation[index_operator[-1]+1:index_equation[-1]+1])
                    element_equation[index_operator[-1]+1:index_equation[-1]+1] = [group_elements]
                    index_equation[:] = []
                    index_equation[:] = []
                    n -=1

                # if more than 1 operator
                elif len(index_operator) >=2:
                    double_operator = index_operator[n+1]-index_operator[n]
                    end_index_operator = index_operator[n+1]
                    dif_start_index_equation = end_index_operator - start_index_operator
                    # for double operator : ** or //
                    if double_operator == 1 and element_equation[index_operator[n]] in expo_floor_operators and element_equation[index_operator[n+1]] in expo_floor_operators:
                        end_index_operator = index_operator[n+1]
                        stack_operator = element_equation.pop(end_index_operator)
                        element_equation[index_operator[n]] = element_equation[index_operator[n]] + stack_operator 
                        index_operator[:] = []
                        index_equation[:] = []
                        n-=1
                    #  if not ** or //
                    elif double_operator == 1:
                        print("\033[1;31mDouble operator in equation, enter a valid equation.\033[0m")
                        return main()
                    # regroup midle elements
                    elif dif_start_index_equation >=2:
                        group_elements = "".join(element_equation[start_index_operator+1:end_index_operator])
                        element_equation[start_index_operator+1:end_index_operator] = [group_elements]
                        index_operator[:] = []
                        index_equation[:] = []
                    else:
                        index_operator[:] = []  
                        index_equation[:] = []
                        # n -= 1
                n +=1    
                # if n+1 error, this function is ok
    except IndexError:
        return element_equation


#Function to get user input
def ask_equation():
    user_input = input("Enter your equation : ")
    #analyze input to separate different types (operators, int and floats)
    position_list_equation = 0
    element_equation = list(user_input)
    valid_operators = ["+","-","*","/","%","**","//"]
    grouped_equation = concat(element_equation,valid_operators)
    expo_floor_operators = ["*","/"]
    list_number = search_number()
    try :  
        while position_list_equation < len(grouped_equation):
        
            if "." in grouped_equation[position_list_equation] :
                grouped_equation[position_list_equation] = float(grouped_equation[position_list_equation])
            elif grouped_equation[position_list_equation] in valid_operators:
                grouped_equation[position_list_equation] = str(grouped_equation[position_list_equation])
            elif grouped_equation[position_list_equation] in list_number:
                grouped_equation[position_list_equation] = int(grouped_equation[position_list_equation])

            else:
                ValueError
                print("Input character error, enter a valid equation")
                return ask_equation()
            position_list_equation+=1
        return tuple(grouped_equation)
    except IndexError:
        print("Error, too many operators in a row")
        ask_equation()

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
    while "/" in equation_list:
        position = equation_list.index("/")
        calculation= equation_list[position-1] / equation_list[position+1]
        equation_list[position-1:position+2] = [calculation] 
    return tuple(equation_list)


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

    while "**" in equation_list:
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
    try:
        updated_equation = exponentiation(equation)
        updated_equation = multiplication(updated_equation)
        updated_equation = division(updated_equation)
        updated_equation = modulus(updated_equation)
        updated_equation = floor_division(updated_equation)
        updated_equation = addition(updated_equation)
        updated_equation = substraction(updated_equation)
    except TypeError:
        print("\033[1;31mError : 2 operators in a row\033[0m")
        main()
    except ZeroDivisionError:
        print('\033[1;31mDivision/Modulus by zero impossible\033[0m')
        main()
    return updated_equation

#Main program loop
def main():

    create_history()

    choice = menu()

    if choice == "1": #ask for equation and carry out calculation
        user_equation = ask_equation()
        final_result = priority(user_equation)
        user_equation = str(user_equation)
        history = {user_equation : final_result}

        #add equation to history
        with open("history.json", "r") as file:
            history = json.load(file)
        if user_equation in history:
            if isinstance(history[user_equation], list):
                history[user_equation].append(final_result)
        else:
            history[user_equation] = [final_result]

        with open("history.json", "w") as file:
            json.dump(history, file)

        print(f"{user_equation} = {final_result}")
        main()

    elif choice == "2": #view calculator history
        with open("history.json", "r") as file:
            history = json.load(file)
            print("\n\033[1;34mHere is the history: ")
        if history:
            for equation, result in history.items():
                print(f"{equation} = {result}")
        else:
            print("\nNo history found")
        main()
    
    elif choice == "3": #delete history
        with open("history.json", "w") as file:
            history = json.dump({}, file)
            print("\n\033[1;32mHistory has been deleted.\033[0m")
        main()
    
    elif choice == "4":
        print("\nBye bye!")
        exit()
    
    else:
        print("\033[1;31mInvalid choice, please try again.\033[1;0m")
        main()

    

# the main function 
if __name__ == "__main__":
    main()


