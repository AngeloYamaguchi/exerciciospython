from time import sleep
print("aperte o enter para iniciar a contagem regressiva")

for c in range(10,-1, -1):
    print(c)
    sleep(1)

print("Bum! "* 10)
