global numbers
numbers =("ZER","ONE","TWO","THR","FOU","FIV","SIX","SEV","EIG","NIN")
operators = ("+", "-", "*")
def str_to_num(nums):
    if nums in numbers:
        return numbers.index(nums)

a = input()
print(str_to_num(a))
