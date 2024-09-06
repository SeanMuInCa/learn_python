age = input("input your age: ")
def check_age(age_input): return 2024 - int(age_input)

year = check_age(age)
print()
print('you were born in ',year)
if year > 2000: print('you are too young')
if year > 1990: print('you are old enough')
else: print('you are too old')


