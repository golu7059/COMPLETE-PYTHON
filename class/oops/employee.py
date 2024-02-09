# create a class having three instance variables and increament by 15% of the salary
class emp:
      name  = "golu kumar"
      age = "60"
      salary = 35000

      def increment(self):
            self.salary = self.salary*1.15

emp1 = emp()
print(emp1.salary)
emp1.increment()
print(emp1.salary)

print(emp.__dict__)