n = int(input("Enter the number : "))
reversedNumber = 0
while n>0:
    reversedNumber = reversedNumber*10 + n%10
    n=n//10
 
print(reversedNumber)