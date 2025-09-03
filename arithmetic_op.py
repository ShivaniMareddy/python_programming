'''def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def pro(a,b):
    return a*b
def quo(a,b):
    return a/b
def rem(a,b):
    return a%b
def floor(a,b):
    return a//b
def exp(a,b):
    return a**b
a=5
b=2
print("Addition",add(a,b))
print("Subtraction",sub(a,b))
print("Product",pro(a,b))
print("Division",quo(a,b))
print("Floor division",floor(a,b))
print("Exponent",exp(a,b))
print("Remainder",rem(a,b))
'''
def func(a,b):
    add=a+b
    sub=a-b
    pro=a*b
    quo=a/b
    rem=a%b
    floor=a//b
    exp=a**b
    return (add,sub,pro,quo,rem,floor,exp)
op=func(5,2)
for i in op:
    print(i)