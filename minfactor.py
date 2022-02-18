def factor(n):
    if (n%2==0):
        return 2
    i = 3
    while (i*i<=n):
        if (n%i==0):
            return i
        i+=2
    return n


n=350
x=factor(n)
print(n-x)
