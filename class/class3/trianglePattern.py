a = int(input("Enter the number : "))

for i in range(1,a+1) : 
    for m in range(i,a) : 
        print(" " , end="")
    for j in range(1,i+1) :
        print(j , end="")
    for k in range(i-1,0,-1):
        print(k ,end="")
    print()
