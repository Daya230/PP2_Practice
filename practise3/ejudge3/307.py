from math import sqrt
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")
    def move(self, new_x,new_y):
        self.x = new_x
        self.y = new_y
    
    def length(self, ot_point):
        dx = self.x - ot_point.x
        dy =  self.y - ot_point.y
        return sqrt(dx**2+dy**2)

x1,y1 = map(int,input().split())
p1 = Point(x1,y1)
p1.show()
x2,y2 = map(int,input().split())
p1.move(x2,y2)
p1.show()
x3,y3 = map(int,input().split())
p2 = Point(x3,y3)
distance = p1.length(p2)
print(f"{distance:.2f}")
        