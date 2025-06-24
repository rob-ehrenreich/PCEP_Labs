#PCAP 2.4.1.6 LAB A LED Disaply

#Program that simulates the work of a seven segment display LED device
#Should display any non-negative integer number entered by the user
#Added exception handling for anything other than non-zero integers entered

hsh = "#"
chsh = "# #"
lhsh = "#  "
rhsh = "  #"
hsh3 = hsh*3
digit_height = 5

reps = {
    "0": (hsh3,chsh,chsh,chsh,hsh3),
    "1": (rhsh,rhsh,rhsh,rhsh,rhsh),
    "2": (hsh3,rhsh,hsh3,lhsh,hsh3),
    "3": (hsh3,rhsh,hsh3,rhsh,hsh3),
    "4": (chsh,chsh,hsh3,rhsh,rhsh),
    "5": (hsh3,lhsh,hsh3,rhsh,hsh3),
    "6": (hsh3,lhsh,hsh3,chsh,hsh3),
    "7": (hsh3,rhsh,rhsh,rhsh,rhsh),
    "8": (hsh3,chsh,hsh3,chsh,hsh3),
    "9": (hsh3,chsh,hsh3,rhsh,hsh3)
}

def sevseg():
    global usernum
    valid_flag = False
    while valid_flag == False:
        try:
            usernum = input("Enter a positive integer number: ")
            usernum = int(usernum)
            digits = [reps[digit] for digit in str(usernum)]
            for i in range(digit_height):
                print(" ".join(segrow[i] for segrow in digits))
                valid_flag=True
        except ValueError:
            for ndx,ch in enumerate(usernum):
                if ch not in reps.keys():
                    print(f"{ch} at position {ndx+1} invalid, please try again")
                    valid_flag=False
    return
              

sevseg()
