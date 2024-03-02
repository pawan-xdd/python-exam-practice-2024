def palindrome():
    txt = input("Enter a string: ") #accepts your input
    rev = txt[::-1] #reverses the text
    if rev == txt: #checks whether rev and txt are same or not
        print(f"{txt} is Palindrome") # this will be printed if txt is equal to rev
    else:
        print(f"{txt} is Not Palindrome.") #if not, this will be printed
    return rev #will print the reversed text


while True:
    print("Type 1 to continue, 0 to exit.")
    action = input("Enter your action: ")
    match action:
        case '1':
           txt = palindrome()
           print(txt)
        case '0':
            break 
    