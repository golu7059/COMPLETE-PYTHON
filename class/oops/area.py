class Area:
    def __init__(self,radius):
        self.radius = radius
    def cal(self):
        self.area = 3.14*(self.radius**2)
        return self.area
    def __init__ (self,length,width):
        self.length = length
        self.width = width
    def rectangleArea(self):
        self.area = self.length*self.width
        return self.area

circle1 = Area(10)
print(circle1.cal())

reactangle1 = Area(10,20)
print(reactangle1.rectangleArea())