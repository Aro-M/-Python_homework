
ch = input("Enter  a value ")
if len(ch) == 1:
    if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
    or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
        print(ch, "is a Vowel")
    else:
        print(ch, "is a Consonant")
else:
    print("The value you entered is greater than one")