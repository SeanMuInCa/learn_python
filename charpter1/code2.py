age = input("input your age: ")
def check_age(age): return 2024 - int(age)

year = check_age(age)
print()
print('you were born in ',year)
if year > 2000: print('you are too young')
else: print('you are old enough')

