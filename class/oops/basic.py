class student:
    def __init__ (self, name , rollNo, age):
        self.name = name 
        self.rollNo = rollNo
        self.age = age

    def display(self):
        print(self.name)
        print(self.rollNo)
        print(self.age)

student1 = student("Golu",2,21)
student2 = student("rathi",49,32)
student3 = student("anand",51,20)

print("NAME : ",student1.name ,"and age is : ",student1.age)
print("NAME : ",student2.name ,"and age is : ",student2.age)
print("NAME : ",student3.name ,"and age is : ",student3.age)