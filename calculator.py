from operations import sum, subctract, multiply, divide

def calculation():
    first_number = int(input("Inserisci un numero"))
    # while type(first_number) != "<class 'int'>":
    #     first_number = input("Reinserici un valore valido ")

    second_number = int(input("Inserisci un altro numero"))
    operation = input("Inserisci un'operatore")
    
    if(operation == "+"):
        return sum(first_number, second_number)
    elif(operation == "-"):
        return subctract(first_number, second_number)
    elif(operation == "*"):
        return multiply(first_number, second_number)
    elif(operation == "/"):
        return divide(first_number, second_number)
    
print("Il risultato è ", calculation())
