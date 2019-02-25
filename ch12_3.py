#http://tinyurl.com/gpqe62e
class Triangle():
    def __init__(self,base,height):
        self.base = base
        self.height = height
    def area(self):
        return self.height * self.base / 2

a_triangle = Triangle(20,30)
print(a_triangle.area())
