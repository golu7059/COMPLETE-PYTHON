age = float(input("Enter your age : "))    # here, if we not convert age into float or int then it will give errors
                                           # because without this . age will be treated as a string .

if age >= 18:
    print("You are an adult .")
    print("Congratulations! you are eligible for voting")

elif age > 0 and age < 18 :
    print("You are currently not eligible for voting.")
    print("Please wait " + str(18-age) + " years .")

else :
    print("Given data can't be a age . Please enter a correct age .")

print("Thank You ")