import random
r = random.randint(10,30)

while(True):
    inp = int(input())
    if(inp < r):
        print("Wrong guess , try a greather number. ")
    elif(inp > r):
        print("Wront guess , try a less number .")
    else:
        print("Congratulations ! you entered a wright guess .")
        break