#declarando las variables de entrada
n,m = map(int, input().split())
cad = input().split()
arrLol = [1 if x == "LOL" else 0 for x in cad]
#print(A)
acuml = [0] * n
acuml[0] = arrLol[0]
for i in range(1, n):
    acuml[i] = acuml[i - 1] + arrLol[i]

for j in range (10):
    #6 8 
    inicio, fin = map(int, input().split())
    #5
    inicio = inicio - 1
    #7
    fin = fin - 1
    #4
    lol = acuml[fin]
    if inicio > 0: 
        # = 4 - acuml[5 - 1]
        # = 4 - acuml[4]
        # = 4 - 3
        # 1
        lol = lol - acuml[inicio - 1]
    # = 7 - 5 + 1 -1
    # 2
    dota = fin - inicio + 1 - lol
    # 1 = 2
    if lol == dota:
        print("AFK")
    # 1 > 2
    elif lol > dota:
        print("LOL")
    else:
        print("DOTA")
