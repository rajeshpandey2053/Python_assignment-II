def func1(li):
    return li[0]

def func2(li):
    return li[1]

def func3(li):
    return li[2]


my_tuple = ('rajesh', 'pandey', 23)
people = []
people.append(my_tuple)
print("After first tuple is added to list: ",people)
friend_tuple1 = ('hari', "chaudhary", 34)
friend_tuple3 = ('gopal', 'karki' , 76)
people.append(friend_tuple1)
print("After second tuple is added to list: ",people)
people.append(friend_tuple3)
print("After third tuple is added to list: ",people)

sorted_age = sorted(people, key=func1)
print("sorted list according to first_name is: ", sorted_age)

sorted_age = sorted(people, key=func2)
print("sorted list according to last_name is: ", sorted_age)

sorted_age = sorted(people, key=func3)
print("sorted list according to age is: ", sorted_age)
