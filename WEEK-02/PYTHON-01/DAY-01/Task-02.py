'''2.Prompt user to enter a value between 1 to 100 and print out the grade based on rules below
            # >= 90 and <= 100 : Grade A
            # >= 80 and < 90 : Grade B
            # >= 70 and < 80 : Grade C
            # < 70 : Grade F'''


marks = int(input("Enter a value between 1 to 100 ::"))
if(marks >= 90 and marks<=100):
    print("Grade A")
elif(marks >= 80 and marks <= 90):
    print("Grade B")
elif(marks>=70 and marks<=80):
    print("Grade C")
else:
    print("Grade F")
