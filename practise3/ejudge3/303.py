numbers = ("ZER","ONE","TWO","THR","FOU","FIV","SIX","SEV","EIG","NIN")
operators = "+-*"

def str_to_num(s):
    digits = []
    for i in range(0, len(s), 3):
        digits.append(str(numbers.index(s[i:i+3])))
    return int("".join(digits))

def num_to_str(n):
    return "".join(numbers[int(d)] for d in str(n))

expr = input()

for op in operators:
    if op in expr:
        left, right = expr.split(op)
        a = str_to_num(left)
        b = str_to_num(right)

        if op == "+":
            res = a + b
        elif op == "-":
            res = a - b
        else:
            res = a * b

        print(num_to_str(res))
        break
