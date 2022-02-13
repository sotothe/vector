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
        self._start = start  # Weak data hiding
        self.__end = end     # Strong data hiding

    @property
    def end(self):
        return self.__end

    @end.setter
    def end(self, value):
        if type(value) == Point:
            if value.x > self._start.x:
                self.__end = value
        elif type(value) == tuple:
            p = Point(value[0],value[1])
            if p.x > self._start.x:
                self.__end = p

    @staticmethod
    def i():
        return Vector(Point(0,0), Point(1,0))

    @classmethod
    def j(cls):
        return cls(Point(0,0), Point(0,1))

    def __str__(self):
        return f'{self._start} -> {self.__end}'

    def length(self):
        dx = self.__end.x - self._start.x
        dy = self.__end.y - self._start.y
        return sqrt((dx**2)+(dy**2))

    def __add__(self, other):
        dx_self = self.__end.x - self._start.x
        dx_other = other.__end.x - other._start.x
        dy_self = self.__end.y - self._start.y
        dy_other = other.__end.y - other._start.y
        dx = dx_self + dx_other
        dy = dy_self + dy_other
        end = Point(self._start.x + dx, self._start.y + dy)
        return Vector(self._start, end)

    def __eq__(self, other):
        dx_self = self.__end.x - self._start.x
        dx_other = other.__end.x - other._start.x
        dy_self = self.__end.y - self._start.y
        dy_other = other.__end.y - other._start.y
        dx = dx_self == dx_other
        dy = dy_self == dy_other
        return dx and dy

    def __invert__(self):
        return Vector(self.__end, self._start)

    def __sub__(self, other):
        return self + (~other)



# def i():
#     return Vector(Point(0,0), Point(1,0))

# v1 = Vector(Point(6,9), Point(8,5))
# v2 = Vector(Point(5,5), Point(7,6))
# print(v1)
# print(v2)
# print((v1 + v2).length())
# print(v1 == v2)
# print(~v1)
# print(v1 - v2)

# print(Vector.color)
# print(Vector.i())
# print(Vector.j())


v1 = Vector(Point(6,9), Point(8,5))
# v1.__end = Point(2,3)
# v1.end = Point(6,3)
v1.end = (12,3)
print(v1)
# print(v1.__end)