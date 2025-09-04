#using temporary var
a=int(input("Enter a:"))
b=int(input("Enter b:"))
temp=a
a=b
b=temp
print('a value',a)
print('b value',b)
#without temp
c=10
d=20
print("Before Swapping")
print('c=',c)
print('d=',d)
(c,d)=(d,c)
print("Before Swapping")
print('c=',c)
print('d=',d)