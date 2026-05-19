n=int(input("input n: "))
assert n>0
try:
    p=1/2
    for i in range(2,n+1):
        p=(1/(i+1))*p
    print(f'p={p}')
except AssertionError:
    print("number less than 0")