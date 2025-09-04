def currentbill(tu):
    if(tu<=50):
        bill=tu*3.80
    elif(tu>=51 and tu<=100):
        bill=(50*3.80)+((tu-50)*4.20)
    elif(tu>=100 and tu<=200):
        bill=(50*3.80)+(50*4.20)+((tu-100)*5.10)
    elif(tu>=201 and tu<=300):
        bill=(50*3.80)+(50*4.20)+(100*5.10)+((tu-200)*6.30)
    else:
        bill=(50*3.80)+(50*4.20)+(100*5.10)+(100*6,30)+((tu-300)*7.50)
    return bill
pmr=int(input("Present month reading:"))
lmr=int(input("Last month reading:"))
tu=pmr-lmr
total=currentbill(tu)
print(total)
