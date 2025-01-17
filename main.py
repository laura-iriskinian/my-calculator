import json

#Create Json file to load history into
file_name = "History.json"

def load_history():
    with open(file_name, "r") as file:
        return json.load(file)

#Save history to file with Json
def save_history(history):
    with open(file_name, "w") as file:
        json.dump(history, file)
            

# condition for calculation including ZeroDivision
def calculation (number_1,operator,number_2):
    try:
        if operator == "+":
            return number_1 + number_2
        elif operator == "-":
            return number_1 - number_2
        elif operator == "*":
            return number_1 * number_2
        elif operator == "/":
            return number_1 / number_2
        elif operator == "%":
            return number_1 % number_2
        elif operator == "**":
            return number_1 ** number_2
        elif operator == "//":
            return number_1 // number_2
    except ZeroDivisionError:
            return "Division or modulus by 0 impossible"

# checks if the input is a number and transforms it to the correct format
def ask_number_1():
    try:
        number_1 = input("Number 1 : ")
        if "." in number_1 or "," in number_1 :
            return float(number_1.replace(",","."))
        else:
            return int(number_1)
    except ValueError:
        print("\nInput error, enter one or more numbers\n")
        return ask_number_1()

# checks if the input is an operator 
def ask_operator():
    
        operator = input("Operator : ")
        valid_operators = ["+","-","*","/","%","**","//"]

        if operator in valid_operators:
            return operator
        else:
            ValueError
            print("\nInput error, enter a valid operator")
            question = input("\nDo you want to display the list of operators ? \
                             \nAnswer with Y or N : ")
            if question.upper() == "Y":
                print("\nHere are the valid operators : \nAddition : + \nSubstraction : - \
                      \nMultiplication : * \nDivision : / \nModulus : % \nExponentiation : **  \nFloor division : // \n")
                return ask_operator()
            else:
                return ask_operator()

# checks if the input is a number and transforms it to the correct format
def ask_number_2():
    try:
        number_2 = input("Number 2 : ")
        if "." in number_2 or "," in number_2 :
            return float(number_2.replace(",","."))
        else:
            return int(number_2)
    except ValueError:
        print("Input error, enter one or more numbers")
        return ask_number_2()

# def for return the number and operator input 
def ask():
    number_1 = ask_number_1()
    operator = ask_operator()
    number_2 = ask_number_2()  
    return number_1,operator,number_2


def menu():
    print ("\n\033[0m1. Use the calculator\n2. View history \n3. Delete history \n4. Exit the program")
    
    return input("\nYour choice (1-4) : ")

def main():
    # choice 1-4
    choice = menu()

    # calculation + add the result to the historical folder 
    if choice == "1":
        number_1,operator,number_2 = ask()
        result = calculation(number_1,operator,number_2)

        #convert expression list into Json string
        history = load_history()
        history.append(f"{number_1} {operator} {number_2} = {result}")
        save_history(history)

        print(f"\n\033[93m{number_1} {operator} {number_2} = {result}\n\033[0m")
        main()

    # read the historical folder 
    elif choice == "2":
        history = load_history()
        print("\n\033[1;34mHere is the history:")
        if history:
            for record in history:
                print(record)
        else:
            print("No history found.")
        main()

    # reset the history folder with ""
    elif choice == "3":
        save_history([])
        print("\n\033[1;32mHistory has been deleted.\033[0m")
        main()

    # exit the program
    elif choice == "4":
        exit()

    else:print("\nError, please make a choice between 1 and 4")
    return main()
    

# the main def 
if __name__ == "__main__":
    main()
