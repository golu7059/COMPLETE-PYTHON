number1 = input("Enter the first number : ")
number2 = input("Enter the second number : ")

# sum = number1 + number2   (this will print as it is . So, in python it is compulsory to use the data type converesion)

sum = int(number1) + int(number2)

print("Sum of these two numbers is : " + str(sum) )  #here we have also to convert sum into string . Because it is in "int" formate and we can't concatanate integers with strings
