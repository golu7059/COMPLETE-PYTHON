n = input("Enter the number : ")
n= n.strip().lower()
temp = n[::-1]

if(n == temp):
    print("Yes it's palindrome")
else :
    print("Not palindrome")



