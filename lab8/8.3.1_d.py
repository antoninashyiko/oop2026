def problem_d(n):
    a1 = 0
    a2 = 1
    s = 0
    for i in range(1,n+1):
        a=a2+i*a1
        a2=a1
        a1=a
        s+=2**i*a
        yield s
n=int(input("Enter a number: "))
try:
    if n<0:
        raise AssertionError
    for elem in problem_d(n):
        print(elem)
except AssertionError:
    print("n is less then 0")
