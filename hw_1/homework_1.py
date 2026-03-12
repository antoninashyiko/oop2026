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
class Rectangle:
    def __init__(self, a, b):
        assert a>0 and b>0
        self.a=a
        self.b=b
    def perimeter(self):
        return 2*(self.a+self.b)
    def area(self):
        return self.a*self.b
class Circle:
    def __init__(self, r):
        assert r>0
        self.r=r
    def length(self):
        return 2*self.r*3.14
    def area(self):
        return 3.14*self.r*self.r
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
class Trapeze:
    def __init__(self, a, b, c, d):
        assert a>0 and b>0 and c>0 and d>0
        self.a=a
        self.b=b
        self.c=c
        self.d=d
    def perimeter(self):
        return self.a+self.b+self.c+self.d
    def area(self):
        sp=(self.a+self.b)*((self.a+self.b-self.c+self.d)*(self.a+self.b+self.c-self.d)*(self.a-self.b+self.c+self.d)*(self.a-self.b+self.c-self.d))**(0.5)/4*(self.a-self.b)
        return sp

smax1=0
pmax1=0
name1=" "
k1=0
with open("input01.txt", 'r') as f:
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
                p=t.length()
                s=t.area()
            if d[0]=='Parallelogram':
                t=Parallelogram(int(d[1]), int(d[2]), int(d[3]))
                p=t.perimeter()
                s=t.area()
            if d[0]=='Trapeze':
                t=Trapeze(int(d[1]), int(d[2]), int(d[3]), int(d[4]))
                p=t.perimeter()
                s=t.area()
            if type(s) != complex:
                if int(s) > int(smax1) and p>pmax1:
                    name1=d[0]
                    k1=t
        except AssertionError:
            pass
smax2=0
pmax2=0
k2=0
name2=" "
with (open("input02.txt", 'r') as f):
    lines=f.readlines()
    for l in lines:
        d=l.split()
        try:
            if d[0]=='Triangle':
                t=Triangle(int(d[1]), int(d[2]), int(d[3]))
                p=t.perimeter()
                s=t.area()
            if d[0]=='Rectangle':
                t =Rectangle(int(d[1]), int(d[2]))
                p=t.perimeter()
                s=t.area()
            if d[0]=='Circle':
                t=Circle(int(d[1]))
                p=t.length()
                s=t.area()
            if d[0]=='Parallelogram':
                t=Parallelogram(int(d[1]), int(d[2]), int(d[3]))
                p=t.perimeter()
                s=t.area()
            if d[0]=='Trapeze':
                t=Trapeze(int(d[1]), int(d[2]), int(d[3]), int(d[4]))
                p=t.perimeter()
                s=t.area()
            if type(s) != complex:
                if int(s) > int(smax2) and int(p)>int(pmax2):
                    name2=d[0]
                    k2=t
        except AssertionError:
            continue

smax3=0
pmax3=0
name3=" "
k3=0
with open("input03.txt", 'r') as f:
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
                p=t.length()
                s=t.area()
            if d[0]=='Parallelogram':
                t=Parallelogram(int(d[1]), int(d[2]), int(d[3]))
                p=t.perimeter()
                s=t.area()
            if d[0]=='Trapeze':
                t=Trapeze(int(d[1]), int(d[2]), int(d[3]), int(d[4]))
                p=t.perimeter()
                s=t.area()
            if type(s) != complex:
                if int(s)>int(smax3) and int(p)>int(pmax3):
                    name3=d[0]
                    k3=t
        except AssertionError:
            continue
# якщо трапеція то виведе лише перші три сторони
print("in input01.txt the biggest area and perimeter: ", name1, k1.a, k1.b, k1.c)
print("in input02.txt the biggest area and perimeter: ", name2, k2.a, k2.b, k2.c)
print("in input03.txt the biggest area and perimeter: ", name3, k3.a, k3.b, k3.c)