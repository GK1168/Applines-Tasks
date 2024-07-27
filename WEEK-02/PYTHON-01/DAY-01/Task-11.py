#.Prompt user to enter a number and print out all the odd, even numbers between 0 and the number separately on two



number = int(input("Enter a number::"))

odd_list = [x for x in range(0,number) if x%2!=0]
even_list = [x for x in range(0,number) if x%2==0]

print(f"Even list : {even_list}\nOdd list : {odd_list}")