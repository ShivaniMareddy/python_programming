def no_in_words(n):
    words={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
    for i in str(n):
        print(words[int(i)],end=" ")
no_in_words(121)