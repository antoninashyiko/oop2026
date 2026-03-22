class Triangle:
    def __init__(self, a, b, c):
        assert a + b > c and a + c > b and c + b > a
        self.a=a
        self.b=b
        self.c=c

    def perimeter(self):
        p=(self.a+self.b+self.c)
        return p
    def area(self):
        P=self.perimeter()/2
        s=(P*(P-self.a)*(P-self.b)*(P-self.c))**(0.5)
        return s
    def __str__(self):
        return f"Triangle: {self.a, self.b, self.c}, Perimeter: {self.perimeter()}, Area: {self.area()}"

class Rectangle:
    def __init__(self, a, b):
        assert a>0 and b>0
        self.a=a
        self.b=b
    def perimeter(self):
        return 2*(self.a+self.b)
    def area(self):
        return self.a*self.b
    def __str__(self):
        return f"Rectangle: {self.a, self.b}, Perimeter: {self.perimeter()}, Area: {self.area()}"

class Circle:
    def __init__(self, r):
        assert r>0
        self.r=r
    def perimeter(self):
        return 2*self.r*3.14
    def area(self):
        return 3.14*self.r*self.r
    def __str__(self):
        return f"Circle: {self.r}, Perimeter: {self.perimeter()}, Area: {self.area()}"

class Parallelogram:
    def __init__(self, a, b, c):
       assert a>0 and b>0 and c>0 and c<b # c - висота, проведена до а
       self.a=a
       self.b=b
       self.c=c
    def perimeter(self):
         return 2*(self.a+self.b)
    def area(self):
         return self.a*self.c
    def __str__(self):
        return f"Parallelogram: {self.a, self.b, self.c}, Perimeter: {self.perimeter()}, Area: {self.area()}"

class Trapeze:
    def __init__(self, a, b, c, d):
        assert a>0 and b>0 and c>0 and d>0
        assert a!=b
        self.a=a
        self.b=b
        self.c=c
        self.d=d
    def perimeter(self):
        return self.a+self.b+self.c+self.d
    def area(self):
        assert (self.a+self.b-self.c+self.d)*(self.a+self.b+self.c-self.d)*(self.a-self.b+self.c+self.d)*(self.a-self.b+self.c-self.d)>0
        sp=(self.a+self.b)*((self.a+self.b-self.c+self.d)*(self.a+self.b+self.c-self.d)*(self.a-self.b+self.c+self.d)*(self.a-self.b+self.c-self.d))**(0.5)/(4*(self.a-self.b))
        return sp
    def __str__(self):
        return f"Trapeze: {self.a, self.b, self.c, self.d}, Perimeter: {self.perimeter()}, Area: {self.area()}"

def find_max(filename):
    smax = 0
    pmax = 0
    k = 0
    with open(filename, 'r') as f:
        lines=f.readlines()
        for l in lines:
            d=l.split()
            try:
                if d[0]=='Triangle':
                    t=Triangle(int(d[1]), int(d[2]), int(d[3]))
                    p=t.perimeter()
                    s=t.area()
                if d[0]=='Rectangle':
                    t=Rectangle(int(d[1]), int(d[2]))
                    p=t.perimeter()
                    s=t.area()
                if d[0]=='Circle':
                    t=Circle(int(d[1]))
                    p=t.perimeter()
                    s=t.area()
                if d[0]=='Parallelogram':
                    t=Parallelogram(int(d[1]), int(d[2]), int(d[3]))
                    p=t.perimeter()
                    s=t.area()
                if d[0]=='Trapeze':
                    t=Trapeze(int(d[1]), int(d[2]), int(d[3]), int(d[4]))
                    p=t.perimeter()
                    s=t.area()
                if s> smax and p>pmax:
                    k=t
                    smax=s
                    pmax=p
            except AssertionError:
                pass
    return k

t1=find_max('input01.txt')
t2=find_max('input02.txt')
t3=find_max('input03.txt')
print("input01.txt: ", t1)
print("input02.txt: ", t2)
print("input03.txt: ", t3)
