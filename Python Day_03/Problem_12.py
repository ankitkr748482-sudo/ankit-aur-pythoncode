# check whether character is vowel and uppercase 

char = input("Enter a character:")

if char in  'AEIOU ':
    print("This is uppercase vowel alphabet")
else:
    if char in 'aeiou':
        print("This is lowercase vowel alphabet")
    else:
        print("This is not a vowel")