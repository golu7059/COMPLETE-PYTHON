size = int(input("Enter the length of the list : "))
elements = []  #  declered a empty list 
for i in range(size) :
    elements.append(input())

print(elements)
idx1 = int(input("Enter the index1 : "))
idx2 = int(input("Enter the index2 : "))

temp = elements[idx1]
elements[idx1] = elements[idx2]
elements[idx2] = temp

print(elements)