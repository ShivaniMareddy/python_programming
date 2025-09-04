def armstrong(n):
    s=str(n)
    sum=0
    for i in s:
        sum+=int(i)**len(s)
    if(sum==n):
        return "Armstrong"
    else:
        return "Not armstrong"
print(armstrong(153))