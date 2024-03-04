def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


terms = int(input("Enter number of terms to be printed: "))
f = []
element = int(input("Enter the element to be accessed: "))
print("Fibonacci sequence:")
for i in range(terms):
    # print(fibonacci(i))
    f.append(fibonacci(i))

print(f"The {element}th term in the Fibonacci series is {f[element]}")
print("---------------------------------------------------------------------")
print("Would you like to print the entire series ? \n y/n")
action = input()
if action.startswith("y"):
    for i in range(terms):
        print(fibonacci(i))
elif action.startswith("n"):
    exit("Bye!")