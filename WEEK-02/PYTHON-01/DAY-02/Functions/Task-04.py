'''Prices of an item across multiple days is provided as a list. Calculate which combination of purchase, sale price yields maximum profit.
         [123, 189, 202, 91, 254, 289]
         Note:You have to buy an item before you sell'''
         

cp_list = list(map(int,input("Enter cost prices list ::").split(',')))
sp_list = list(map(int,input("Enter selling prices list :: ").split(',')))

print(f"List of Cost prices : {cp_list} \nList of Selling prices : {sp_list}")

def plList(cp_list,sp_list):
    pl = []
    if(len(cp_list) == len(sp_list)):
        for i in range(len(cp_list)):
            pl.append((sp_list[i] - cp_list[i]))
    return pl

proloss_list = plList(cp_list,sp_list)
print(f"profit/loss list : {proloss_list} -- Max profit : {max(proloss_list)}")
        
