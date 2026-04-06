import math as m
class Figure:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
class Two_d(Figure):
    def dimention(self):
        return "two dimensional"
    def perimeter(self):
        return 1
    def area(self):
        return 2
    def volume1(self):
        return 2
    def squareSurface(self):
        return None
    def squareBase(self):
        return None
    def height(self):
        return None
    def volume(self):
        return None
class Three_d(Figure):
    def dimention(self):
        return "three dimensional"
    def perimeter(self):
        return None
    def area(self):
        return None
    def squareSurface(self):
        return 1
    def squareBase(self):
        return 2
    def height(self):
        return self.a #come back to edit!!!
    def volume(self):
        return 3
class Triangle(Two_d):
    def __init__(self, a, b, c):
        assert a + b > c and a + c > b and c + b > a
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        p=self.a+self.b+self.c
        return p
    def area(self):
        p0=(self.a+self.b+self.c)/2
        s=((p0-self.a)*(p0-self.b)*(p0-self.c)*p0)**0.5
        return s
    def __str__(self):
        return f"Triangle: {self.a, self.b, self.c}, Area: {self.area()}"
class Rectangle(Two_d):
    def __init__(self, a, b):
        assert a>0 and b>0
        self.a = a
        self.b = b
    def perimeter(self):
        p=(self.a+self.b)*2
        return p
    def area(self):
        s=self.a*self.b
        return s
    def __str__(self):
        return f"Rectangle: {self.a, self.b}, Area: {self.area()}"
class Trapeze(Two_d):
    def __init__(self, a, b, c, d):
        assert a > 0 and b > 0 and c > 0 and d > 0 and (a+b-c+d)*(a+b+c-d)*(a-b+c+d)*(a-b+c-d)>0
        assert a!=b
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def perimeter(self):
        p=self.a+self.b+self.c+self.d
        return p
    def area(self):
        s=(self.a + self.b) * ((self.a + self.b - self.c + self.d) * (self.a + self.b + self.c - self.d) * (self.a - self.b + self.c + self.d) * (self.a - self.b + self.c - self.d)) ** (0.5) / (4 * (self.a - self.b))
        return s
    def __str__(self):
        return f"Trapeze: {self.a, self.b, self.c, self.d}, Area: {self.area()}"
class Parallelogram(Two_d):
    def __init__(self, a, b, c):
        assert a > 0 and b > 0 and c>0
        self.a = a
        self.b = b
        self.c = c #height to a
    def perimeter(self):
        p=(self.a+self.b)*2
        return p
    def area(self):
        s=self.a*self.c
        return s
    def __str__(self):
        return f"Parallelogram: {self.a, self.b, self.c}, Area: {self.area()}"
class Circle(Two_d):
    def __init__(self, a):
        assert a>0
        self.a = a
    def perimeter(self):
        p=2*m.pi*self.a
        return p
    def area(self):
        s=m.pi*(self.a)**2
        return s
    def __str__(self):
        return f"Circle: {self.a}, Area: {self.area()}"
class Ball(Three_d):
    def __init__(self, a):
        assert a > 0
        self.a = a
    def surface_area(self):
        ss=4*m.pi*(self.a)**2
        return ss
    def volume(self):
        sb=4*m.pi*(self.a)**3/3
        return sb
    def __str__(self):
        return f"Ball: {self.a}, Volume: {self.volume()}"
class TriangularPyramid(Triangle, Three_d):
    def __init__(self, a, h):
        assert a > 0 and h>0
        self.a = a
        self.h = h
    def surface_area(self): #площа  поверхні
        s=m.sqrt(3) * self.a ** 2
        return s
    def volume(self): #обʼєм
        v=(m.sqrt(2)*self.a**3)/12
        return v
    def __str__(self):
        return f"TriangularPyramid: {self.a, self.h}, Volume: {self.volume()}"
class QuadrangularPyramid(Rectangle, Three_d):
    def __init__(self, a, b, h):
        assert a > 0 and b>0 and h > 0
        self.a = a
        self.b = b
        self.h = h
    def surface_area(self): #площа  поверхні
        s1=self.a*self.b
        l1=m.sqrt(self.h**2+(self.a/2)**2)
        l2 = m.sqrt(self.h ** 2 + (self.b / 2) ** 2)
        s2=self.a*l1+self.b*l2
        return s1+s2
    def volume(self): #volume
        v=self.a*self.b*self.h/3
        return v
    def __str__(self):
        return f"QuadrangularPyramid: {self.a, self.b, self.h}, Volume: {self.volume()}"
class RectangularParallelepiped(Rectangle, Three_d):
    def __init__(self, a, b, c):
        assert a > 0 and b > 0 and c > 0
        self.a = a
        self.b = b
        self.c = c
    def surface_area(self):
        s=2*(self.a*self.b+self.b*self.c+self.a*self.c)
        return s
    def volume(self):
        v=self.a*self.b*self.c
        return v
    def __str__(self):
        return f"RectangularParallelepiped: {self.a, self.b, self.c}, Volume: {self.volume()}"
class Cone(Circle, Three_d):
    def __init__(self, r, h):
        assert r > 0 and h > 0
        self.r = r
        self.h = h
    def surface_area(self):
        l=m.sqrt(self.r**2+self.h**2)
        s=m.pi*self.r*(self.r+l)
        return s
    def volume(self):
        v=m.pi*self.r**2*self.h/3
        return v
    def __str__(self):
        return f"Cone: {self.r, self.h}, Volume: {self.volume()}"
class TriangularPrism(Triangle, Three_d):
    def __init__(self, a, b, c, h):
        assert a > 0 and b > 0 and c>0 and h > 0
        assert a + b > c and a + c > b and b + c > a
        self.a = a
        self.b = b
        self.c = c
        self.h = h
    def surface_area(self):
        s1=(self.a+self.b+self.c)*self.h
        p=(self.a+self.b+self.c)/2
        s2=m.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
        return s1+2*s2
    def volume(self):
        p = (self.a + self.b + self.c) / 2
        v=m.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))*self.h
        return v
    def __str__(self):
        return f"TriangularPrism: {self.a, self.b, self.c, self.h}, Volume: {self.volume()}"

def find_max(filename):
    smax = 0
    k = None
    with open(filename, 'r') as f:
        lines=f.readlines()
        for l in lines:
            t=None
            s=None
            d=l.split()
            try:
                if d[0]=='Triangle':
                    t=Triangle(int(d[1]), int(d[2]), int(d[3]))
                    s=t.area()
                elif d[0]=='Rectangle':
                    t=Rectangle(int(d[1]), int(d[2]))
                    s=t.area()
                elif d[0]=='Parallelogram':
                    t=Parallelogram(int(d[1]), int(d[2]), int(d[3]))
                    s=t.area()
                elif d[0]=='Trapeze':
                    t=Trapeze(int(d[1]), int(d[2]), int(d[3]), int(d[4]))
                    s = t.area()
                elif d[0]=='Circle':
                    t=Circle(int(d[1]))
                    s = t.area()
                elif d[0]=='Ball':
                    t=Ball(int(d[1]))
                    s = t.volume()
                elif d[0]=='TriangularPyramid':
                    t=TriangularPyramid(int(d[1]), int(d[2]))
                    s = t.volume()
                elif d[0]=='QuadrangularPyramid':
                    t=QuadrangularPyramid(int(d[1]), int(d[2]), int(d[3]))
                    s = t.volume()
                elif d[0]=='RectangularParallelepiped':
                    t=RectangularParallelepiped(int(d[1]), int(d[2]), int(d[3]))
                    s = t.volume()
                elif d[0]=='Cone':
                    t=Cone(int(d[1]), int(d[2]))
                    s = t.volume()
                elif d[0]=='TriangularPrism':
                    t=TriangularPrism(int(d[1]), int(d[2]), int(d[3]), int(d[4]))
                    s = t.volume()
                if s > smax and t is not None and s is not None:
                    k = t
                    smax = s
            except AssertionError:
                pass
    return k

t1 = find_max('input01.txt')
t2 = find_max('input02.txt')
t3 = find_max('input03.txt')
print("input01.txt: ", t1)
print("input02.txt: ", t2)
print("input03.txt: ", t3)