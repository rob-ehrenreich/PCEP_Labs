#PCAP 2.5.1.10 Lab Find a Word!

user1 = input("Enter search word: ")
user2 = input("Enter text string to check: ")

def faw(string1, string2):
    r=0
    st1compare=[]
    count=0
    while r != -1:
        string1=string1.lower()
        string2=string2.lower()
        for ch in string1:
            r=string2.find(ch,count)
            if r<count:
                return "No"
            st1compare.append(ch)
            count=r
        if "".join(st1compare) == string1:
            return "Yes"
    else:
        return "No"

print(faw(user1, user2))
