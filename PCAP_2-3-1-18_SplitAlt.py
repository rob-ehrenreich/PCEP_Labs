#PCAP 2.3.1.18 LAB Your Own Split

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
   
print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
