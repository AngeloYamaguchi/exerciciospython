primeiro = int(input("primeiro termo"))
razão = int(input("Razão"))
decimo = primeiro + (10 -1)*razão
for a in range(primeiro,10,razão):
    print("{}".format(a),end="-")
