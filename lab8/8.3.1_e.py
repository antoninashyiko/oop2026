from math import sin, factorial

x=float(input("input number x: "))
saved=x
n=1
s=0
k=0
while abs(x)>10**-4:
    s+=x
    n+=2
    k+=1
    x = (-1) ** k * saved ** n / factorial(n)
print(f's with taylor: {s}')
print(f'with math.sin: {sin(saved)}')