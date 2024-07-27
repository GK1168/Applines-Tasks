'''Prompt user to enter year, month values and print the calender for the combination.
        Hint: Refer to Calender module.'''


import calendar

year = int(input("Enter year :: "))
month = int(input("Enter month ::"))

print(calendar.month(year,month))
