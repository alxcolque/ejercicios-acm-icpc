t = int(input())
impar = 0
par = 0
while t > 0:
    x = int(input())
    if x % 2 == 0:
        par += 1
    else:
        impar += 1
    t -= 1

if impar > par:
    print("gana Bob")
elif impar < par:
    print("gana Alice")
else:
    print("hay Empate")
