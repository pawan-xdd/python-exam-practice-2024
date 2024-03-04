def factorial(num):
    factorial = 1
    if(num<0):
        print("Factorial number can't be negative.")
    elif(num == 0):
        print("Factorial of 0 is 1")
    else:
        for i in range(1, num+1):
            factorial = factorial * i
        return f"The factorial of {num} is : {factorial}"
            
n = factorial(4)
print(n)