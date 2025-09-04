def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
def func(x):
    s=str(x)
    sum=0
    for i in s:
        sum+=fact(int(i))
    return sum
print(func(1234))
