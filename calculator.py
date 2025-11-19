from operations import sum, subctract, multiply, divide, square, module

operations = {
    "sum": "+",
    "subctract": "-",
    "multiply": "*",
    "divide": "/",
    "square": "**",
    "module": "%"
}

def get_number(prompt):
    
    while True:
        try:
            return float(input(prompt))
        except:
            print("Inserisci un Numero Valido")

def get_operation(prompt):

    operation_values = operations.values()

    while True:
        current_operation = input(prompt)
        if current_operation in operation_values:
                return current_operation
        else:
            print("Inserire un operazione Valida : +, -, /, *, **, %")



first_number = get_number("Inserisci un Numero")
second_number= get_number("Inserisci un Altro Numero")
operation = get_operation("Inserire un operatore per il tipo di operazione...")

def calculator(num1, num2, operation):
    
    if(operation == "+"):
        return sum(num1, num2)
    elif(operation == "-"):
        return subctract(num1, num2)
    elif(operation == "*"):
        return multiply(num1, num2)
    elif(operation == "/"):
        return divide(num1, num2)
    elif(operation == "**"):
        return square(num1, num2)
    elif(operation == "%"):
        return module(num1, num2)

operation_name = ""
for key, value in operations.items():
    if value == operation:
        operation_name= key
        break

print("Il risultato è ", calculator(first_number, second_number, operation))
print("L'operazione eseguita era ", operation_name)

