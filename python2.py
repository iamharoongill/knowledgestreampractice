print("python2")
 
print("harron")


def add(n1, n2):
    return n1+n2

a = 4
b= 5

additionl_sm = add(a, b)

print(additionl_sm)


def find_odd(my_array):
    for i in arr:
        if i%2 !=0:
            print("is odd", i)
        else:
            print(" is even", i)
    for i in range(len(my_array)):
        if my_array[i]%2 !=0:
            print("is odd", my_array[i])
        else:
            print(" is even", my_array[i])

arr = [2,3,6,7,10]

find_odd(arr)


c = input("enter your name: ")

print(c)


def check_is_smal_prime (n1):
    match n1:
        case 2:
            print ("matched with 2")
        case 3:
            print ("matched with 3")
        case 5:
            print ("matched with 5")
        case 7:
            print ("matched with 7")
        case 11:
            print ("matched with 11")
        case _ :
            print("it is not small prime")
        

arr = [2,3,5,7, 11]

find_odd(arr)
c = int(input("Enter a numer: "))

check_is_smal_prime(c)