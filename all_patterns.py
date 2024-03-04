def print_star_pattern(rows):
    for i in range(1, rows + 1):
        print('* ' * i)

def print_inverted_star_pattern(rows):
    for i in range(rows, 0, -1):
        print('* ' * i)

def print_pyramid(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '* ' * i)

def print_inverted_pyramid(rows):
    for i in range(rows, 0, -1):
        print(' ' * (rows - i) + '* ' * i)

def print_diamond(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '* ' * i)
    for i in range(rows - 1, 0, -1):
        print(' ' * (rows - i) + '* ' * i)

def print_hollow_diamond(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '* ' * i)
    for i in range(rows - 1, 0, -1):
        print(' ' * (rows - i) + '* ' * i)

def print_left_aligned_triangle(rows):
    for i in range(1, rows + 1):
        print('* ' * i)

def print_right_aligned_triangle(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '* ' * i)

# Example usage:
rows = 5

print("Star Pattern:")
print_star_pattern(rows)

print("\nInverted Star Pattern:")
print_inverted_star_pattern(rows)

print("\nPyramid Pattern:")
print_pyramid(rows)

print("\nInverted Pyramid Pattern:")
print_inverted_pyramid(rows)

print("\nDiamond Pattern:")
print_diamond(rows)

print("\nHollow Diamond Pattern:")
print_hollow_diamond(rows)

print("\nLeft Aligned Triangle Pattern:")
print_left_aligned_triangle(rows)

print("\nRight Aligned Triangle Pattern:")
print_right_aligned_triangle(rows)
