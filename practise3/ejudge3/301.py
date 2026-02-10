def is_valid_number(n):
    for digit in n:
        if int(digit) % 2 != 0: 
            return "Not valid"
    return "Valid"

n = input()
print(is_valid_number(n))
