from math import sqrt


class  Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'( {self.x}  {self.y} )'


class Vector:
    color = 'blonde'
    def __init__(self, start, end):
        self.start = start
        self.end = end

    @staticmethod
    def i():
        return Vector(Point(0,0), Point(1,0))

    def __str__(self):
        return f'{self.start} -> {self.end}'

    def length(self):
        dx = self.end.x - self.start.x
        dy = self.end.y - self.start.y
        return sqrt((dx**2)+(dy**2))

    def __add__(self, other):
        dx_self = self.end.x - self.start.x
        dx_other = other.end.x - other.start.x
        dy_self = self.end.y - self.start.y
        dy_other = other.end.y - other.start.y
        dx = dx_self + dx_other
        dy = dy_self + dy_other
        end = Point(self.start.x + dx, self.start.y + dy)
        return Vector(self.start, end)

    def __eq__(self, other):
        dx_self = self.end.x - self.start.x
        dx_other = other.end.x - other.start.x
        dy_self = self.end.y - self.start.y
        dy_other = other.end.y - other.start.y
        dx = dx_self == dx_other
        dy = dy_self == dy_other
        return dx and dy

    def __invert__(self):
        return Vector(self.end, self.start)

    def __sub__(self, other):
        return self + (~other)

v1 = Vector(Point(6,9), Point(8,5))
v2 = Vector(Point(5,5), Point(7,6))
print(v1)
print(v2)
print((v1 + v2).length())
print(v1 == v2)
print(~v1)
print(v1 - v2)

print(Vector.color)
print(Vector.i())
