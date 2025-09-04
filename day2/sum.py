def natural_no(n):
    i=1
    sum=0
    while(i<=n):
        sum+=i
        i=i+1
    print("Sum:",sum)
num=int(input("Enter value of n"))
natural_no(num)