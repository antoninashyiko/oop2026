class Rational:
    def __init__(self, n, d):
        assert d!=0
        self.n = int(n)
        self.d = int(d)
        self.symplyfication()
    def nsd(self, a, b):
        if b > a:
            a, b = b, a
        while b != 0:
            a, b = b, a % b
        return a
    def symplyfication(self):
        if self.nsd(self.n, self.d) != 1:
            r=self.nsd(self.n, self.d)
            self.n//=r
            self.d//=r
        if self.d<0:
            self.n*=-1
            self.d*=-1
    def __add__(self, other):
        if isinstance(other, Rational):
            return Rational(self.n*other.d+other.n*self.d, self.d*other.d)
        elif isinstance(other, int):
            return Rational(self.n + other*self.d, self.d)
        else:
            raise TypeError("Rationals can only be added to Rationals or Integers")
    def __str__(self):
        return f'number: {self.n}/{self.d}'
class RationalList:
    def __init__(self):
        self.l=[]
    def add_l(self):
        self.l.append(Rational(self.n, self.d))
    def __getitem__(self, i):
        return self.l[i]
    def __len__(self):
        return len(self.l)
    def __add__(self, other):
        try:
            result = RationalList()
            result.l = self.l.copy()
            result += other
            return result
        except TypeError:
            raise TypeError("Rationals can only be added to Rationals or Integers")
    def __iadd__(self, other):
        if isinstance(other, RationalList):
            self.l.extend(other.l)
            return self
        elif isinstance(other, Rational):
            self.l.append(other)
            return self
        elif isinstance(other, int):
            self.l.append(Rational(other, 1))
            return self
        else:
            raise TypeError("Rationals can only be added to Rationals or Integers")
    def __str__(self):
        return ', '.join(str(x) for x in self.l)

def func(filename):
    with open(filename, 'r') as f:
        a=RationalList()
        lines=f.readlines()
        for l in lines:
            p=l.split()
            for i in range(len(p)):
                try:
                    if '/' in p[i]:
                        n, d=map(int, p[i].split('/'))
                        num=Rational(n, d)
                        a+=num
                    else:
                        num=Rational(int(p[i]), 1)
                        a+=num
                except (TypeError, AssertionError):
                    pass
        return a
def sum_lst(lst):
    s = Rational(0, 1)
    for x in lst:
        s += x
    return s

k1=func('input01.txt')
k2=func('input02.txt')
k3=func('input03.txt')
print("input01.txt", sum_lst(k1))
print(" ")
print("input02.txt", sum_lst(k2))
print(" ")
print("input03.txt", sum_lst(k3))
