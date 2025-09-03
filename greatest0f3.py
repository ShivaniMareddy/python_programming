def greatest(a,b,c):
    if(a>b):
        if(a>c):
            print("a is greatest")
        else:
            print("c is greatest")
    else:
        if(b>c):
            print("b is greatest")
        else:
            print("c is greatest")
greatest(10,20,30)
greatest(10,30,20)
greatest(30,20,10)
