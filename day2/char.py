def char(n):
    if n.isalpha():
        print("Alphabet")
    elif n.isdigit():
        print("Digit")
    else:
        print("Special characters")
char('a')
char('6')