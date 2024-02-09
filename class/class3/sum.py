n = int(input("Enter the number : "))
sum = 0
while(n>0):
    sum+=(n%10)
    n=int(n/10)

print("Cout of all digits is ",sum)
