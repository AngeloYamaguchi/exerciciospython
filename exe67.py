i
while True:
    n = int(input("Tabuada de qual numero Você quer ver?"))
    if n < 0 :
        break
    print("+=" *30)
    for c in range(1,11):
        print(f" {n} X {c} = {n*c}")
    print("+=" * 30)
print(" Fim")
