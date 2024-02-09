name = "Golu Kumar"

print(name.lower())  # this will print name in lower case
print(name.upper())  # this will print name in upper case
print(name)          # but there will no chane in origional name


# finding in string 
print(name.find("G"))        #if found then it will display it's index value(0th based indexing)
print(name.find("g"))        #if not found then it will print -1
print(name.find("Gol"))

#replacing
print(name.replace("Golu","vishal"))
print(name)                   # still no change in origional value of the variable

# To check string or character is a part of variable or not

print("G" in name)
print("g" in name)
print("Golu " in name)
print("Golu  Kumar" in name)     

# these all return boolean values (true / false)