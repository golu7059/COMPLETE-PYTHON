# Taking input from user : firstNumber - operator - secondNumber

first = float(input("Enter first number : "))
operator = input("Enter operator (+ , - , * , / , % ) : ")
second = float(input("Enter second number : "))

# using if-else 
if (operator == "+") :
    print("Addition is : " + str(first + second))       # To print into string formate . Here we have to convert float or int values into string using str()

elif(operator == "-") :
    print("Subtraction is : " + str(first - second))

elif(operator == "*") :
    print("Multiplication is : " + str(first * second))

elif(operator == "/") :
    print("Division is : " + str(first / second))

elif(operator == "%") :
    print("Modulus is : " + str(first % second))

else :
    print("Please enter a valid operator .")