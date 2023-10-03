def new_fun (num , str):
    if str == 'asc':
        a = sorted(num, reverse = False)
        print(a)
    
    elif str == 'dec':
        b = sorted (num, reverse=True)
        print (b)

    elif str == 'none':
        print (num)

    else:
        print("none")

num = [2,20,4,23, 11,98]
str = input("enter the value =")
print (new_fun (num , str))