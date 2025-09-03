num=int(input("Enter consumer number:"))
name=input("Enter consumer name:")
pmr=int(input("Enter present month reading:"))
lmr=int(input("Enter last month reading:"))
tu=pmr-lmr
bill=tu*3.80
print("Consumer number",num)
print("Consumer name",name)
print("Present month reading",pmr)
print("Last month reading",lmr)
print("Total units",tu)
print("Current bill",bill)