if __name__ == "__main__":
    while True:
        try:
            num = int(input("Enter a number: "))
            factorial = 1
            if(num<0):
                print("Factorial number can't be negative.")
            elif(num == 0):
                print("Factorial of 0 is 1")
            else:
                for i in range(1, num+1):
                    factorial = factorial * i
                    print(f"The factorial of {num} is : {factorial}")
        except ValueError as e:
            print(f"{e}")
        
