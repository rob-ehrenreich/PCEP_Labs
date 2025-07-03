class Timer:
    def __init__(self, hours=0, mins=0, secs=0):
        self.__h = hours
        self.__m = mins
        self.__s = secs

    def __str__(self):
        self.__tstring = [str(self.__h), str(self.__m), str(self.__s)]
        
        for i in range(3):
            if len(self.__tstring[i]) == 1:
                self.__tstring[i] = f'{self.__tstring[i]:02}'
        return ':'.join(self.__tstring)

    def next_second(self):
        self.__s += 1
        if self.__s > 59:
            self.__s = 0
            self.__m += 1
            if self.__m > 59:
                self.__m = 0
                self.__h += 1
                if self.__h > 23:
                    self.__h = 0
        return self.__str__

    def prev_second(self):
        self.__s -= 1
        if self.__s == -1:
            self.__s = 59
            self.__m -= 1
            if self.__m == -1:
                self.__m = 59
                self.__h -= 1
                if self.__h == -1:
                    self.__h = 23
        return self.__str__


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
