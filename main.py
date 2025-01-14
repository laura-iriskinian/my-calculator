# condition for calculation
def calculation (number_1,operator,number_2):
    if operator == "+":
        return number_1 + number_2
    elif operator == "-":
        return number_1 - number_2
    elif operator == "*":
        return number_1 * number_2
    elif operator == "/":
        if number_2 != 0:
            return number_1 / number_2
        else: 
            return "division by 0 impossible"
    elif operator == "%":
        if number_2 != 0:
            return number_1 % number_2
        else:  
            return "modulus by 0"
    elif operator == "**":
        return number_1 ** number_2
    elif operator == "//":
        if number_2 != 0:
            return number_1 // number_2
        else: 
            return "division by 0 impossible"

# checks if the input is a number and transforms it to the correct format
def ask_number_1():
    try:
        number_1 = input("number 1 : ")
        if "." in number_1 or "," in number_1 :
            return float(number_1.replace(",","."))
        else:
            return int(number_1)
    except ValueError:
        print("\nInput error, enter one or more digits\n")
        return ask_number_1()

# checks if the input is a operator 
def ask_operator():
    
        operator = input("operator : ")

        if operator == "+" or operator == "-" or operator == "*" or operator == "/" \
            or operator == "%" or operator == "**":
            return operator
        else:
            ValueError
            print("\nInput error, enter one valid operator")
            question = input("\nDo you want to display the list operators ? \
                             \nAnswer with O or N : ")
            if question == "O":
                print("\nHere are the valid operators : \nAddition : + \nSubtraction : - \
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
        print("Input error, enter one or more digits")
        return ask_number_2()

# def for return the number and operator input 
def ask():
    number_1 = ask_number_1()
    operator = ask_operator()
    number_2 = ask_number_2()  
    return number_1,operator,number_2


def menu():
    print ("\n\033[0m1. Use the calculator\n2. View history \n3. Delete l'history \n4. Exit the program")
    return input("\nYour choice (1-4) : ")

def main():
    # choice 1-4
    choice = menu()

    # calculation + add the result to the historical folder 
    if choice == "1":
        number_1,operator,number_2 = ask()
        result = calculation(number_1,operator,number_2)
        folder = open("historical.txt","a")
        folder.write(f"\n{number_1} {operator} {number_2} = {result}")
        folder.close()
        print(f"\n{number_1} {operator} {number_2} = {result}\n")
        main()

    # read the historical folder 
    if choice == "2":
        print("\n\033[1;34mHere is the history :")
        folder = open("historical.txt","r")
        print(folder.read())
        folder.close()
        main()

    # reset the historical folder with ""
    if choice == "3":
        folder = open("historical.txt", "w")
        folder.write("")
        folder.close
        print("\n\033[1;32mThe history has been deleted\033[0m")
        main()

    # exit the program
    if choice == "4":
        exit()

# the main def 
if __name__ == "__main__":
    main()