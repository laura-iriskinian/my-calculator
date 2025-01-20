
#faire la boucle principale (While TRUE)

while True:
    try :
        
     num1 = float(input('entrez le premier chiffre:'))
     op1 = input('operateur(+,-,*,/): ')
     num2 = float(input('entrez le deuxieme chiffre'))
     resultat = ({num1},{op1},{num2})

    except ValueError:
        print('mauvaise saisi')
# differents opperateurs disponnibles

    if op1 =='+':
        resultat = num1 + num2
    elif op1 == '-':
        resultat = num1 - num2
    elif op1 =='*':
        resultat = num1 * num2
    elif op1 == '/':
        if num2 ==0 :
           print('pas de lettre ni de division par zéro')
           continue
        resultat = num1 / num2
    
    print  (resultat)

    print('choisissez votre action:')
    print ("1: continuer")
    print("2: sortir")

    user_choice = int(input())

    if user_choice == 1 :
        print('veuillez entrer de nouveau une valeur')
        
    elif user_choice == 2 :
        print ('au revoir et bonne journée')
        
    break