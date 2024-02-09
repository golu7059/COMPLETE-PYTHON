a = int(input("Enter a number : "))
numberOfDigits = 0

while (a>0) :
    numberOfDigits = numberOfDigits + 1
    a = int(a/10)

print("number of digits are : ", numberOfDigits)
