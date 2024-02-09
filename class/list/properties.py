marks = [96,56,89,99,88]

marks.append(99)       # add element at last

marks.insert(0,102)     # add elements at given index value

print(102 in marks)     # to check specific element is persent or not in list

print(len(marks))       # print total number of elements

# marks.clear()           # delete all elements and make list empty
 
print(marks)

marks.remove(96)
print(marks)

print(marks.pop(0))
print(marks)