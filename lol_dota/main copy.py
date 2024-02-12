n, m = map(int, input().split())
cadena = input().split()
A = [1 if x == "LOL" else 0 for x in cadena]

acc = [0] * n
acc[0] = A[0]
for i in range(1, n):
    acc[i] = acc[i - 1] + A[i]

for j in range(m):
    L, R = map(int, input().split())
    L -= 1
    R -= 1
    lol = acc[R]
    if L > 0:
        lol -= acc[L - 1]
    dota = R - L + 1 - lol

    if lol == dota:
        print("AFK")
    elif lol > dota:
        print("LOL")
    else:
        print("DOTA")
