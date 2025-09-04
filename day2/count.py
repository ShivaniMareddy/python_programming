def countdig(n):
    count=0
    while(n>0):
        if(n%10>0):
            count+=1
            n=n//10
    return count
print(countdig(16723))