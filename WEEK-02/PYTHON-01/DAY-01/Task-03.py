#3.Prompt user to enter an year and print out if it is a leap year or not.



year = int(input("Enter an year::"))
if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print(f"{year} --> Leap Year")
else:
    print(f"{year} --> Not a leap Year")