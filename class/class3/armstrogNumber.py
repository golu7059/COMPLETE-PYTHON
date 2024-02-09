a = int(input("Enter a number : "))
givenNumber = a
sumOfCubeOfDigits = 0
while (a>0) :
    reminder = a%10
    sumOfCubeOfDigits += pow(reminder,3)
    a = int(a/10)

    
if (sumOfCubeOfDigits == givenNumber) :
    print("Yes it's  a Armstrong number")
else : 
    print("Not a armstrong number")