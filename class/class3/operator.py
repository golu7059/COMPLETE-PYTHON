# print(233 and 7 and 9 and 8 or 11)
# print(bin(5))
# print(bin(7))
# print(5 & 7)
# print(5>7 or 6<4)

# print("a" in "apple")
# a = [2,3]
# b = [2,3]

# print(a is b)

# d = {(1,2) : "one", 2 : "two", 2:"three",4:"four"}
# print(d)
# print(d[2])

# d[2] = "ii"
# print(d[2])

# d = {(1,2) : "one", 2 : "two", 2:"three",4:"four"}
# print(d)
# print(d[2])

# employee = {'employee1' : [1001 , "vatshal" ,80000], 'employee2': [1002,"Anand",20114], 'employee3': [1003,"Rathi",200]}
# print(employee['employee2'])
# print(employee)
# try to change the name of the specific employee

# if 0 : 
#     print("wrong")
# else : 
#     print("Right")

# for i in range(0,10,2) :
#     if i==4 :
#         continue
#     print(i)

# given number is prime or not
a=7
isPrime = True
for i in range(2,int(a/2)) :
    if(a%i == 0 ) :
       isPrime= False
    
if isPrime : 
    print("it's a prime number")
else :
    print("it's not a prime number")