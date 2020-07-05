def is_prime(a):
    x = True 
    for i in range(2, a):
       if a%i == 0:
           x = False
           break 
    if x:
        print( "True")
    else:
        print ("False")

num = int(input("Enter the number: "))
is_prime(num)