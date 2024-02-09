def factorial(num):
    if(num == 0 or num == 1):
        return 1
    return num*factorial(num-1)

input = int(input("Enter the number : ")) 
ans = factorial(input)
print(f"The factorial of number {input} is {ans}.")
