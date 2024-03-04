def print_star_pattern(rows):
    for i in range(1, rows + 1):
        print('* ' * i)
        
rows = int(input("Enter number of rows: "))

print("Star Pattern:")
print_star_pattern(rows)
