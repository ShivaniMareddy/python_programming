def palindrome(n):
    for i in range(1,n+1):
        s=str(i)
        if(s==s[::-1]):
            print(i)
palindrome(150)