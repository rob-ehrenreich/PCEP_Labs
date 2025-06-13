def mysplit(strng):
    global mlst
    word=''
    mlst=[]
    strng.strip()
    for ch in strng:
        if ch.isspace() and word!='':
            mlst.append(word)
            word=''
        elif ch.isspace() and word =='':
            continue
        else:
            word = word + ch
    return mlst
    #
    # put your code here
    #


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))