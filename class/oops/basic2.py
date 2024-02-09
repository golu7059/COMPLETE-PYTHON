#find the output
class a:
    z=10
    def __init__(self):
        self.z = 40
    def b(self):
        a.k=30

a.l = 50
a1 = a()
# print(a.z)
#print(a.__dict__)

class sample:
     i = 10
     def __init__(self):
         sample.i = 20

s1 = sample()
s1.i = 30
print(sample.i)
print(s1.i)

