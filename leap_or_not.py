def leap(a):
    if(a%4==0 and a%100!=0):
        print("Leap year")
    elif(a%100==0 and a%400==0):
        print("Leap year")
    else:
        print("Not leap year")
leap(2025)
leap(2024)
