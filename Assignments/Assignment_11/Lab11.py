'''
CS 101 Lab
Program 11
Levi Lindskog is my name in Canvas, but I go by Levi Estabrook.
lhl8r5@umsystem.edu

PROBLEM:
Program must accept input of hour, minute, and second,
and then output the curent time every second.
Program must utilize class for Clock,
and import time module for proper incrementation.
Program must be able to be able to function in 24 hour mode or 12 hour mode,
depending on an optional parameter input.

ERROR HANDLING:
__str__() method was printing out result instead of returning it, resulting in error,
resolved by changing print statements to return statements.
'''

#ALGORITHM

import time

class Clock:
    def __init__(self,hours,minutes,seconds,clock_type = 0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.clock_type = clock_type

    def __str__(self):
        if self.clock_type == 0:
            return '{:02d}:{:02d}:{:02d}'.format(self.hours,self.minutes,self.seconds)
        else:
            if 0 <= self.hours <= 11:
                label = 'am'
            elif 12 <= self.hours <= 23:
                label = 'pm'
            else:
                label = 'FIXME'
            if self.hours == 0:
                return '{:02d}:{:02d}:{:02d} {}'.format(self.hours + 12,self.minutes,self.seconds,label)
            elif 1 <= self.hours <= 12:
                return '{:02d}:{:02d}:{:02d} {}'.format(self.hours,self.minutes,self.seconds,label)
            else:
                return '{:02d}:{:02d}:{:02d} {}'.format(self.hours - 12,self.minutes,self.seconds,label)

    def tick(self):
        self.seconds += 1
        if self.seconds >= 60:
            self.seconds = 0
            self.minutes += 1
            if self.minutes >= 60:
                self.minutes = 0
                self.hours += 1
                if self.hours >= 24:
                    self.hours = 0


if __name__ == "__main__":
    hours = int(input('What is the current hour ==> '))
    minutes = int(input('What is the current minute ==> '))
    seconds = int(input('What is the current second ==> '))

    clock = Clock(hours,minutes,seconds,1)

    while True:
        print(clock)
        clock.tick()
        time.sleep(1)