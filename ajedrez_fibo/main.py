
t = int(input())
while t > 0:
    
    n = int(input())
    a = 0
    b = 1
    c = 0
    for i in range(1, n+1):
        c=a+b
        a=b
        b=c
    # Insert code here
    print(c)
    t -= 1

