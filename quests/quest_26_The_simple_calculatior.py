
def calculator(a,b,operation):
    if operation == "+":
        return a+b
    elif operation == "-":
        return a-b
    elif operation == "*":
        return a*b
    elif operation == "/":
        return a/b

    elif operation == "%":
        return a%b

    else:
         return "Invalid operation"
     
number1=float(input("Enter the first number: "))
number2=float(input("Enter the second number: "))
operation= input("Enter the operation:" )
result=calculator(number1,number2,operation)
print (result)