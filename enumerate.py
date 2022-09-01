idades = [15,18 ,37, 45, 56, 32, 49, 37]
#for i in range (len(idades)):
#print(i, idades)
print(idades.sort())
print(list(reversed(idades)))
print(sorted(idades,reverse = True))

for idades in sorted(idades):
    print(idades)