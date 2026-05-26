def problem_c(n):
    a1 = 2
    a2 = 1
    if n == 1:
        yield a1
    if n == 2:
        yield a2
    for i in range(3, n + 1):
        a3=2 * a2 - 3 * a1
        yield a3
        a1=a2
        a2=a3
n=int(input("Enter a number: "))
try:
    if n<0:
        raise AssertionError
    for elem in problem_c(n):
        print(elem)
except AssertionError:
    print("n is less then 0")
