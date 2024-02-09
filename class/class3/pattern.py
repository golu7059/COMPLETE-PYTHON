n = int(input("Enter the number : "))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    print("*"*i)

print("\t")

for i in range(1,n+1):
    for j in range(n-i):
        print(" ")
    print("*")
    