#PCAP 2.5.1.7 LAB Palindromes

"""
Ask user for text, check whether entered text is a palindrome.
Don't include spaces in the check and an empty string is a not a plaindrome
"""
pal = "It's a palindrome"
npal = "It's not a palindrome"

def reverse_string(x):
    return x[::-1]

def palcheck(txtstring):
    s = txtstring.replace(" ","")
    r = reverse_string(s)
    if s.lower() == r.lower():
        print(pal)
    else:
        print(npal)
    return

userin = input("Enter string to test: ")

if userin == "" or userin.replace(" ","") == "":
    print(npal)
else:
    palcheck(userin)
