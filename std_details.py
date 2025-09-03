num=int(input("Enter student number:"))
name=input("Enter student name:")
phy=int(input("Enter physics marks"))
che=int(input("Enter chemistry marks"))
mat=int(input("Enter maths marks"))
print("Student number:",num)
print("Student Name:",name)
print("Physics",phy)
print("Chemistry",che)
print("Maths",mat)
total=phy+che+mat
print("Total",total)
avg=total/3
print("Average",round(avg,2))