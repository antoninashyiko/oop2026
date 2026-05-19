# problem a
k=int(input("input n: "))
x=float(input("input x: "))
a=x
assert k>0
try:
    for i in range(2, k+1):
        a=(x-x/i)*a
    print(f'a={a}')
except AssertionError:
    print("number less than 0")