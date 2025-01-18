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

def search_number():
    create_number = 0
    list_number = []
    while create_number <= 10000:
        list_number.append(str(create_number))
        create_number+=1
    return list_number

#Function to get user input
def ask_equation():
    user_input = input("Enter your equation : ")
    #analyze input to separate different types (operators, int and floats)
    position = 0
    listed_equation = list(user_input)
    valid_operators = ["+","-","*","/","%","**","//"]
    expo_floor_operators = ["*","/"]
    list_number = search_number()
    try :  
        while position < len(listed_equation):
        
            if "." in listed_equation[position] :
                listed_equation[position] = float(listed_equation[position])
            elif listed_equation[position] in expo_floor_operators and listed_equation[position+1] in expo_floor_operators:
                bla = listed_equation.pop(position+1)
                listed_equation[position] = listed_equation[position] + bla
            elif listed_equation[position] in valid_operators:
                listed_equation[position] = str(listed_equation[position])
            elif listed_equation[position] in list_number:
                listed_equation[position] = int(listed_equation[position])
            else:
                ValueError
                print("Input character error, enter a valid equation")
                return ask_equation()
            position+=1
        return tuple(listed_equation)
    except IndexError:
        print("error, too many operators in a row")
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
        print("Error : 2 operators in a row")
        main()
    except ZeroDivisionError:
        print('Division/Modulus by zero impossible')
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

    

# the main function 
if __name__ == "__main__":
    main()


