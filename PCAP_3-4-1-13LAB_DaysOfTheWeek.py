class WeekDayError(Exception):
    pass
	

class Weeker:
    
    def __init__(self, day):
        self.__daynums = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
        if day not in self.__daynums:
            raise WeekDayError
        self.__day = self.__daynums.index(day)
        self.__wks = 0
        self.__edayi = 0

    def __str__(self):
        return self.__daynums[self.__day]

    def add_days(self, n):
        self.__wks = n // 7
        if n + self.__day < 7:
            self.__day = self.__day + n
        else:
            self.__day = (n % 7) + self.__day
        return self.__str__
            
    def subtract_days(self, n):
        self.__wks = n // 7
        if (self.__day + 1) - n > -1:
            self.__day = self.__day - n
        else:
            self.__day = self.__day - (n % 7)
            if self.__day < 0:
                self.__day += 7
        return self.__str__
            
try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
