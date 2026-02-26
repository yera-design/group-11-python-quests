# I defined a function with three parameters which are a,b and operator
def calculator(a,b,operation):
    #This are defined cases of the  operators i know and things they do to produce the outcome
    if operation == "+":
        return a+b
    elif operation == "-":
        return a-b
    elif operation == "*":
        return a*b
    elif operation == "/":
        if b != 0:
            return a / b
        else:
            print("The second number should not be zero")
    elif operation == "%":
        return a % b
    else:
        return "Invalid operation"
     
number1=float(input("Enter the first number: "))
number2=float(input("Enter the second number: "))
operation= input("Enter the operation:" )
result=calculator(number1,number2,operation)
print (result)