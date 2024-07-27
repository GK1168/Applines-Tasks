'''Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
      Once 'done' is entered, print out the largest and smallest of the numbers.
      If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.'''




list = []
while(True):
    try:
        
        inp = input("Enter either a number or done :: ")
        if (inp != "done"):
        
            list.append(int(inp))
        else:
            print(f"Given list : {list} --> Max : {max(list)} \t Min : {min(list)}")
            break; 
    except:
        print("invalid")
        continue