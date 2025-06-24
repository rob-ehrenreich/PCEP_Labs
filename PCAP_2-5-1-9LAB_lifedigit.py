#PCAP 2.5.1.9 LAB The Digit of Life

def lifedigit(userbd):
    global ldig
    ldig = 0
    for n in str(userbd):
        ldig += int(n)
    #Check if double digit number
    if ldig > 9:
        ldig = ldig % 10 + ldig // 10
    
    return ldig

vf=False
while vf==False:
    try:
        ubd = int(input('Enter your birthday, numbers only. e.g. MMDDYYYY: '))
        vf=True
    except:
        print('Invalid entry, please enter only numbers')
        vf=False

lidig = lifedigit(ubd)
print(f'Your digit of life is: {lidig}')
