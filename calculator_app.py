
def my_add(n1,n2):
    return n1+n2
    
def my_subtract(n1, n2):
    return n1 - n2

def my_multiply(n1, n2):
    return n1 * n2

def my_divide(n1, n2):
    return n1 / n2




print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:

    choose = int(input("Select operations form 1, 2, 3, 4:"))
    

    a = int(input("Enter first number : " ))
    b = int(input("Enter second number : " ))



    if choose == 1:
        print(a, "+", b, "=", my_add(a, b))
        
    elif choose == 2:
        print(a, "-", b, "=", my_subtract(a, b))
        
    elif choose == 3:
        print(a, "*", b, "=", my_multiply(a, b))
        
    elif choose == 4:
        print(a, "/", b, "=", my_divide(a, b))  
        
        
    continue_cal = input("do you want to continue? yes or no: ")
    if continue_cal == "no":
          break
    
    else:
        print("Invalid input")

