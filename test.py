def calculation(number_1, operator, number_2):
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

def find_matching_parenthesis(expression, start_idx):
    count = 1
    i = start_idx + 1
    while i < len(expression):
        if expression[i] == '(':
            count += 1
        elif expression[i] == ')':
            count -= 1
            if count == 0:
                return i
        i += 1
    raise ValueError("Mismatched parentheses")

def parse_expression(expression):
    # Remove spaces and prepare for parsing
    expression = expression.replace(" ", "")
    numbers = []
    operators = []
    current_number = ""
    i = 0
    
    while i < len(expression):
        char = expression[i]
        if char.isdigit() or char == "." or char == ",":
            current_number += char.replace(",", ".")
        elif char == '(':
            # Find matching closing parenthesis
            closing_idx = find_matching_parenthesis(expression, i)
            # Recursively evaluate the expression inside parentheses
            sub_numbers, sub_operators = parse_expression(expression[i+1:closing_idx])
            sub_result = calculate_with_precedence(sub_numbers, sub_operators)
            if current_number:
                # Handle implicit multiplication: 2(3) -> 2 * (3)
                numbers.append(float(current_number))
                operators.append('*')
                current_number = ""
            numbers.append(sub_result)
            i = closing_idx
        elif char in "+-*/%":
            if current_number:
                numbers.append(float(current_number))
                current_number = ""
            operators.append(char)
        elif char == "*" and i + 1 < len(expression) and expression[i + 1] == "*":
            if current_number:
                numbers.append(float(current_number))
                current_number = ""
            operators.append("**")
            i += 1
        elif char == "/" and i + 1 < len(expression) and expression[i + 1] == "/":
            if current_number:
                numbers.append(float(current_number))
                current_number = ""
            operators.append("//")
            i += 1
        i += 1
    
    if current_number:
        numbers.append(float(current_number))
    
    return numbers, operators

def calculate_with_precedence(numbers, operators):
    if not numbers:
        return 0
    if not operators:
        return numbers[0]
    
    # First pass: handle ** operations
    i = 0
    while i < len(operators):
        if operators[i] == "**":
            numbers[i] = calculation(numbers[i], operators[i], numbers[i + 1])
            numbers.pop(i + 1)
            operators.pop(i)
        else:
            i += 1
    
    # Second pass: handle * / % // operations
    i = 0
    while i < len(operators):
        if operators[i] in ["*", "/", "%", "//"]:
            numbers[i] = calculation(numbers[i], operators[i], numbers[i + 1])
            numbers.pop(i + 1)
            operators.pop(i)
        else:
            i += 1
    
    # Third pass: handle + - operations
    i = 0
    while i < len(operators):
        numbers[i] = calculation(numbers[i], operators[i], numbers[i + 1])
        numbers.pop(i + 1)
        operators.pop(i)
    
    return numbers[0]

def ask_expression():
    try:
        expression = input("Enter your calculation (e.g., (2 + 3) * 4): ")
        numbers, operators = parse_expression(expression)
        if not numbers or (operators and len(numbers) - 1 != len(operators)):
            raise ValueError
        return expression, numbers, operators
    except ValueError:
        print("\nInput error, please enter a valid expression")
        return ask_expression()

def menu():
    print("\n\033[0m1. Use the calculator\n2. View history\n3. Delete history\n4. Exit the program")
    return input("\nYour choice (1-4): ")

def main():
    choice = menu()
    
    try:
        if choice == "1":
            expression, numbers, operators = ask_expression()
            result = calculate_with_precedence(numbers, operators)
            folder = open("historical.txt", "a")
            folder.write(f"\n{expression} = {result}")
            folder.close()
            print(f"\n{expression} = {result}\n")
            main()
    except KeyboardInterrupt:
        print("\n Back to menu")    
        
    try:    
        if choice == "2":
            print("\n\033[1;34mHere is the history:")
            folder = open("historical.txt", "r")
            print(folder.read())
            folder.close()
            main()
    except KeyboardInterrupt:
        print("\nBack to menu")    
        return main()
    
    try :    
        if choice == "3":
            folder = open("historical.txt", "w")
            folder.write("")
            folder.close()
            print("\n\033[1;32mThe history has been deleted\033[0m")
            main()
    except KeyboardInterrupt:
        print("\n Back to menu")    
        return main()
    
    if choice == "4":
        exit()
    
    else :
        print ("Make sure to pick a number between 1 and 4")
        return main()

if __name__ == "__main__":
    main()