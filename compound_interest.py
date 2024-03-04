def compound_interest(principal, rate, time, compounding_periods):
    amount = principal * (1 + rate / compounding_periods) ** (compounding_periods * time)
    interest = amount - principal
    return amount, interest

# Example usage:
principal = 1000  # initial principal amount
rate = 0.05  # annual interest rate (5%)
time = 5  # time in years
compounding_periods = 1  # number of times interest is compounded per year

amount, interest = compound_interest(principal, rate, time, compounding_periods)
print(f"Principal amount: ${principal}")
print(f"Interest rate: {rate * 100}%")
print(f"Time (years): {time}")
print(f"Compounding periods per year: {compounding_periods}")
print(f"Total amount after {time} years: ${amount:.2f}")
print(f"Interest earned: ${interest:.2f}")