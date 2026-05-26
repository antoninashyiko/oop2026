def problem_b(k):
    for i in range(2, k+1):
        yield (1/(i+1))
n=int(input("input n: "))
try:
    if n<0:
        raise AssertionError
    p=1/2
    for elem in problem_b(n):
        p*=elem
        print(f'p={p}')
except AssertionError:
    print("number less than 0")
