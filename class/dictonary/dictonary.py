marks = {"physics" : 99 , "chemistry":97, "hindi":90,"maths":98}

print(marks["chemistry"])     # printing marks of specific subject
print(marks.get("chemistry"))

# adding new key:value pair
marks["sports"] = 88

print(marks)
print(len(marks))
print(type(marks))

print(marks.keys()) 
print(marks.values())

marks["sports"] = 100
print(marks)

another_marks = {"java" : 81 , "DBMS" : 91 , "pyhton" : 78}
marks.update(another_marks)
print(marks)

marks.pop("java")
marks.popitem()
print(marks)

# marks.clear()
# print(marks)

# for x in marks : 
#     print(x)
#     print(marks[x])

# for x,y in marks.items() : 
#     print(x,y)

phones = {
    "Area1" : {
        "x" : 0,
        "y" : 1, 
        "z": 3
    },
    "Area2" : {
        "x" : 4,
        "y" : 15, 
        "z": 35
    },
    "Area3" : {
        "x" : 50,
        "y" : 51, 
        "z": 53
    }
}

print(phones["Area1"]["y"])