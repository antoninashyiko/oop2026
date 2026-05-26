from math import sin, factorial
def problem_e(x):
    saved = x
    n = 1
    s = 0
    k = 0
    while abs(x) > 10 ** -4:
        s += x
        yield s
        n += 2
        k += 1
        x = (-1) ** k * saved ** n / factorial(n)
x=float(input("input number x: "))
for elem in problem_e(x):
    result=elem
print(f's with taylor: {result}')
print(f'with math.sin: {sin(x)}')
