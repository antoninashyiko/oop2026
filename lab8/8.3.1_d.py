n=int(input("Enter a number: "))
assert n>10
a1=0
a2=1
s=0
try:
    for i in range(1,n+1):
        a=a2+i*a1
        a2=a1
        a1=a
        s=s+2**i*a
    print("an", a)
    print("ans", s)
except AssertionError:
    print("n is less then 0")