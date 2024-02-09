marks = [96,56,89,99,88]
print(marks[1])
print(marks[4])
print(marks[-1])
print(marks[-0])

# here positive number starts counting from starting through index value (from 0) and negative number start counting from behind without index value (starting with 1)

# to print whole list we can also use for loop
for score in marks:
    print(score , end = " ")

# marks[1 : 4 ] = {"raja"}
# print()
# print(marks) 
print()
goodMarks = [i for i in marks if 80<i<=100]
goodMarks.sort(reverse = True)
print(goodMarks)