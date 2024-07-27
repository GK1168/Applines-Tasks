'''Write a python program to calculate no.of days between 2 dates.
        Sample dates: (2014,7,2) , (2014, 7, 11)
        Expected output: 9 days'''



import datetime
import math

date1 = list(map(int,input("Enter first date:: ").split('-')))
date1 = datetime.date(date1[0],date1[1],date1[2])
print(date1)
date2 = list(map(int,input("Enter first date:: ").split('-')))
date2 = datetime.date(date2[0],date2[1],date2[2])
print(date2)

datediff = abs(date1-date2)
print(f"Difference between {date1} and {date2} :: {datediff.days}")