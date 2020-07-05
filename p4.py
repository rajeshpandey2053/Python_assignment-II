new_list = []
print(id(new_list))
new_list.append('ram')
new_list.append('hari')
new_list.append('gopal')
print(id(new_list))
new_list.sort()
print("the first item on sorted list is: ", new_list[0])
print("The second item on list is: ", new_list[1])