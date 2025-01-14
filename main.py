
def calcul (number_1,operator,number_2):
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
            return "division par 0 impossible"
    elif operator == "%":
        if number_2 != 0:
            return number_1 % number_2
        else:  
            return "modulo par 0"
    elif operator == "**":
        return number_1 ** number_2
    elif operator == "//":
        if number_2 != 0:
            return number_1 // number_2
        else: 
            return "division par 0 impossible"

def demande_number_1():
    try:
        number_1 = input("nombre 1 : ")
        if "." in number_1 or "," in number_1 :
            return float(number_1.replace(",","."))
        else:
            return int(number_1)
    except ValueError:
        print("\nErreur de saisie, rentrez un ou plusieurs chiffres\n")
        return demande_number_1()

def demande_operator():
    
        operator = input("operateur : ")

        if operator == "+" or operator == "-" or operator == "*" or operator == "/" \
            or operator == "%" or operator == "**":
            return operator
        else:
            ValueError
            print("\nErreur de saisie, rentrez un opérateur valide")
            question = input("\nVoulez-vous afficher la liste des opérateurs ? \
                             \nRépondez par O ou N : ")
            if question == "O":
                print("\nVoici les opérateurs valides : \nAddition : + \nSoustraction : - \
                      \nMultiplication : * \nDivision : / \nModulo : % \nPuissance : **  \nDivision entière : // \n")
                return demande_operator()
            else:
                return demande_operator()


def demande_number_2():
    try:
        number_2 = input("nombre 2 : ")
        if "." in number_2 or "," in number_2 :
            return float(number_2.replace(",","."))
        else:
            return int(number_2)
    except ValueError:
        print("Erreur de saisie, rentrez un ou plusieurs chiffres")
        return demande_number_2()

def demande():
    number_1 = demande_number_1()
    operator = demande_operator()
    number_2 = demande_number_2()  
    return number_1,operator,number_2


def menu():
    print ("\n\033[0m1. Utiliser la calculatrice \n2. Voir l'historique \n3. Supprimer l'historique \n4. Quitter le programme")
    return input("\nQue souhaitez vous faire ? ")

def main():

    choice = menu()

    if choice == "1":
        number_1,operator,number_2 = demande()
        resultat = calcul(number_1,operator,number_2)
        folder = open("data.txt","a")
        folder.write(f"\n{number_1} {operator} {number_2} = {resultat}")
        folder.close()
        print(f"\n{number_1} {operator} {number_2} = {resultat}\n")
        main()

    if choice == "2":
        print("\n\033[1;34mVoici l'historique :")
        folder = open("data.txt","r")
        print(folder.read())
        folder.close()
        main()

    if choice == "3":
        folder = open("data.txt", "w")
        folder.write("")
        folder.close
        print("\n\033[1;32mL'historique à bien été supprimé\033[0m")
        main()

    if choice == "4":
        exit()
if __name__ == "__main__":
    main()