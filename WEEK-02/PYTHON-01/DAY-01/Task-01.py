#  1.Calculate tax payable for a given income. Prompt user to enter a positive number.



income = int(input("Enter the person's income:: "))
tax = int(input("Enter the gov tax (percent)::"))
tot_tax = (income * tax)/100
print(f"Person's income : {income}\nGov tax :: {tax}\nTotal tax amount person has to pay ::{tot_tax}")