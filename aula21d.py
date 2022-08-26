def fatorial(n=1):
    f =1
    for c in range(n, 0, -1):
        f *= c
        return f




f1 = fatorial(7)
f2 = fatorial(5)
f3 = fatorial(2)
print(f' oresultados são {f1}, {f2} e {f3}')
