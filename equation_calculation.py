import json

file_name = "history.json"

#Set a function to create json file to save history
def create_history():
    try:
        with open("history.json","x") as file:
            json.dump([], file)
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
    position_list_equation = 0
    element_equation = list(user_input)
    valid_operators = ["+","-","*","/","%","**","//","(",")"]
    expo_floor_operators = ["*","/"]
    list_number = search_number()
    try :  
        while position_list_equation < len(element_equation):
        
            if "." in element_equation[position_list_equation] :
                element_equation[position_list_equation] = float(element_equation[position_list_equation])
            elif element_equation[position_list_equation] in expo_floor_operators and element_equation[position_list_equation+1] in expo_floor_operators:
                bla = element_equation.pop(position_list_equation+1)
                element_equation[position_list_equation] = element_equation[position_list_equation] + bla
            elif element_equation[position_list_equation] in valid_operators:
                element_equation[position_list_equation] = str(element_equation[position_list_equation])
            elif element_equation[position_list_equation] in list_number:
                element_equation[position_list_equation] = int(element_equation[position_list_equation])
            else:
                ValueError
                print("Input character error, enter a valid equation")
                return ask_equation()
            position_list_equation+=1
        return tuple(element_equation)
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

    
# Fonction qui gère les parenthèses et effectue les calculs selon la priorité
def priority(equation):
    equation_list = list(equation)  # Convertir l'équation en liste
    
    # Tant qu'il y a des parenthèses à traiter
    while '(' in equation_list:
        # Trouver les indices de la parenthèse ouvrante et fermante
        start_index = equation_list.index('(')
        end_index = equation_list.index(')')
        
        # Extraire l'équation à l'intérieur des parenthèses
        sub_equation = equation_list[start_index + 1:end_index]
        
        # Effectuer les calculs dans les parenthèses
        sub_equation_result = list(perform_operations(sub_equation))
        
        # Remplacer l'expression entre parenthèses par son résultat
        equation_list = equation_list[:start_index] + sub_equation_result + equation_list[end_index + 1:]
    
    # Une fois toutes les parenthèses traitées, effectuer les calculs restants
    final_result = perform_operations(equation_list)
    
    return tuple(final_result)

# Fonction auxiliaire pour effectuer les opérations selon la priorité
def perform_operations(equation):
    # On s'assure que l'entrée est une liste
    equation_list = list(equation)
    # D'abord traiter l'exponentiation
    equation_list = exponentiation(equation_list)
    # Puis traiter multiplication, division, et le modulo
    equation_list = multiplication(equation_list)
    equation_list = division(equation_list)
    equation_list = modulus(equation_list)
    # Traiter la division entière
    equation_list = floor_division(equation_list)
    # Enfin addition et soustraction
    equation_list = addition(equation_list)
    equation_list = substraction(equation_list)
    
    return tuple(equation_list)  # Retourner la liste mise à jour

#Main program loop
def main():

    create_history()

    choice = menu()

    if choice == "1": #ask for equation and carry out calculation
        user_equation = ask_equation()
        final_result = priority(user_equation)

        #add equation to history
        with open("history.json", "r") as file:
            history = json.load(file)
        history.append(f"{user_equation} = {final_result}")
        with open("history.json", "w") as file:
                json.dump(history, file)

        print(f"{user_equation} = {final_result}")
        main()

    elif choice == "2": #view calcuklator history
        with open("history.json", "r") as file:
            history = json.load(file)
            print("\n\033[1;34mHere is the history: ")
        if history:
            for entry in history:
                print(entry)
        else:
            print("\nNo history found")
        main()
    
    elif choice == "3": #delete history
        with open("history.json", "w") as file:
            history = json.dump([], file)
            print("\n\033[1;32mHistory has been deleted.\033[0m")
        main()
    
    elif choice == "4":
        print("\nBye bye!")
        exit()

    

# the main function 
if __name__ == "__main__":
    main()


