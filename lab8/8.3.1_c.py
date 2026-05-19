n=int(input("Enter a number: "))
assert n>1
try:
    a1=2
    a2=1
    for i in range(3, n+1):
        a=2*a2-3*a1
        a1=a2
        a2=a
    print(a2)
except AssertionError:
    print("n is less then 0")