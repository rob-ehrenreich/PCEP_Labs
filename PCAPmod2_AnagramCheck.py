user1 = input("Enter the first word: ")
user2 = input("Enter the second word: ")

ana = "Anagrams"
nana = "Not Anagrams"

def anacheck(word1, word2):
    w1 = word1.lower()
    w2 = word2.lower()
    if len(word1) != len(word2):
        print(nana)
    elif sorted(w1) == sorted(w2):
        print(ana)
    else:
        print(nana)
    return

if user1 == "" or user1.replace(" ","") == "" or user2 == "" or user2.replace(" ","") == "":
    print(nana)
else:
    anacheck(user1, user2)
