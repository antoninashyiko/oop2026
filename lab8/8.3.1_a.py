# problem a
def problem_a(x, k):
    for i in range(2, k+1):
        yield (x-x/i)

k=int(input("input k: "))
x=float(input("input x: "))
a=x
try:
    if k<0:
        raise AssertionError
    for elem in problem_a(x, k):
        a*=elem
        print(f'elem={elem}')
except AssertionError:
    print("number less than 0")
