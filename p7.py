from functools import reduce



new_list = [('ram', "bahadur", 34), ('gopal','sharma', 56),('krishna','bhat', 3),('none','bahadur',None)]
count = 0
sum = 0
for new in new_list:
    if new[2]!=None:
        sum+=new[2]
        count+=1
avg = sum/count

for find_age in new_list:
    if find_age[2]!=None:
        if find_age[2]>avg:
            print('old')
        else: 
            print("young")

