def passorfail(n):
    if(n>=40):
        print("Pass")
        if(n<=50):
            print("Grade C")
        elif(n>=51 and n<=70):
            print("Grade B")
        elif(n>=71 and n<=80):
            print("Grade A")
        else:
            print("Distension")
    else:
        print("Fail")
passorfail(45)
passorfail(60)
passorfail(72)
passorfail(98)
passorfail(20)