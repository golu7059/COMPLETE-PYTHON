year = int(input("Enter year : "))

if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): 
    print(f"{year} is a Leap Year.")
else :
    print(f"{year} is not an Leap Year.")
