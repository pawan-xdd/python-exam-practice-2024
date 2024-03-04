dividend = int(input("Enter dividend: "))
divisor = int(input("Enter a divisor: "))
try:
    division = dividend/divisor
    print(division)
except ZeroDivisionError:
    exit("ZeroDivisionError : notty hora ke?")
