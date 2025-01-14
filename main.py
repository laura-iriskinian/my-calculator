
def calcul (num1,operator,num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else: 
            return "division par 0 impossible"
    elif operator == "%":
        if num2 != 0:
            return num1 % num2
        else:  
            return "modulo par 0"



def demande_num1():
    try:
        num1 = input("nombre 1 : ")
        if "." or "," in num1:
            return float(num1.replace(",","."))
        else:
            return int(num1)
    except ValueError:
        print("Erreur de saisie, rentrez un ou plusieurs chiffres")
        return demande_num1()


def demande_operator():
    
        operator = input("operateur : ")
        return operator

def demande_num2():
    try:
        num2 = input("nombre 2 : ")
        if "." or "," in num2:
            return float(num2.replace(",","."))
        else:
            return int(num2)
    except ValueError:
        print("Erreur de saisie, rentrez un ou plusieurs chiffres")
        return demande_num1()

def demande():
    num1 = demande_num1()
    operator = demande_operator()
    num2 = demande_num2()  
    return num1,operator,num2



def main():

    num1,operator,num2 = demande()

    resultat = calcul(num1,operator,num2)

    print(f"{num1} {operator} {num2} = {resultat}")


if __name__ == "__main__":
    main()