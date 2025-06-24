#PCAP 2.5.1.6 LAB Improving the Caesar Cipher

upa = ord('A')
upz = ord('Z')
lowa = ord('a')
lowz = ord('z')

welcome = """
******************************************************
* Welcome to the dynamic Caesar Cipher. You will be  *
* asked to enter words to encode and the number of   *
* characters to shift the number. If 0 is entered it *
* will default to 1.                                 *
******************************************************
"""
goodbye = "Goodbye."
print(welcome)
#String to encode
userin = input("Enter Text to Encrypt: ")
#User entered number for amount of cipher shift
valid_flag=False
while valid_flag == False:
    try:
        usernum = int(input('Number (1-25) to shift letters: '))
        if usernum < 0 or usernum > 25:
            print("Incorrect number, please enter a number between 1-25")
            valid_flag = False
        elif usernum == 0:
            usernum = 1
            valid_flag = True
        else:
            valid_flag = True
    except:
        print("Not an integer number, please try again.")
        valid_flag = False

def caesar_encode(userin, usernum=1):
    global cipher
    cipher=''
    for ch in userin:
        if not ch.isalpha():
            cipher += ch
            continue
        code = ord(ch) + usernum
        if ch.islower():
            if code > lowz:
                mod = (code - 1) - lowz
                code = lowa + mod
            cipher += chr(code)
        elif ch.isupper():
            if code > upz:
                mod = (code - 1) - upz
                code = upa + mod
            cipher += chr(code)

    print("")
    print(cipher)
    return cipher

def caesar_decode(scrambled, shiftnum=1):
    global decipher
    decipher=''
    for ch in scrambled:
        if not ch.isalpha():
            decipher += ch
            continue
        decode = ord(ch) - shiftnum
        if ch.islower():
            if decode < lowa:
                mod = lowa - (decode + 1) 
                decode = lowz - mod
            decipher += chr(decode)
        if ch.isupper():
            if decode < upa:
                mod = upa - (decode + 1)
                decode = upz - mod
            decipher += chr(decode)
    return decipher

            


caesar_encode(userin, usernum)
while True:
    print("")
    user_verify = input(f"Would you like to decode, shifting {usernum} letters, and verify? y/n: ")
    try:
        if user_verify.isalpha() and user_verify.lower() == 'y':
            if caesar_decode(cipher, usernum) != userin:
                
                print("\nSomething went wrong - decoded result:")
                print(f" {decipher}")
                print("does not match input:")
                print(f" {userin}")
                print(goodbye)
                break
            else:
                print("\nConfirmed. Decoded result:")
                print(f" {decipher}")
                print("matches input.\n")
                print(goodbye)
                break
        elif user_verify.isalpha() and user_verify.lower() == 'n':
            print("")
            print(goodbye)
            break
        else:
            print("Invalid input, please enter either y or n")
            continue
    except:
        print("Sorry, an error occured")
        
                
