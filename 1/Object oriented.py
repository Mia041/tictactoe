class Cylinder:
    pi=3.14
    def __init__(self,height=1,radius=1):
        self.height=height
        self.radius=radius

    def volume(self):
        return self.radius*self.radius*Cylinder.pi*self.height

    def surface_area(self):
        return Cylinder.pi*2*self.radius*self.height+Cylinder.pi*self.radius*self.radius*2

# EXAMPLE OUTPUT
c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())


import math
class Line:

    def __init__(self,coor1,coor2):
        self.coor1=coor1
        self.coor2=coor2

    def distance(self):

        return math.sqrt((self.coor1[0]-self.coor2[0])**2+(self.coor1[1]-self.coor2[1]))

    def slope(self):
        return (self.coor2[1]-self.coor1[1])/(self.coor2[0]-self.coor1[0])

# EXAMPLE O#UTPUT

coordinate1 = (3,2)
coordinate2 = (8,10)
li = Line(coordinate1,coordinate2)
print(li.distance())
print(li.slope())
