import math
from math import floor

age = input("input your age: ")
def check_age(age_input): return 2024 - int(age_input)

year = check_age(age)
print()
print('you were born in ',year)
if year > 2000: print('you are too young')
if year > 1990: print('you are old enough')
else: print('you are too old')

print(round(0.1 + 0.2, 2))
print(math.floor(1.1 + 0.2))
print(math.ceil(1.1 + 0.2))

str = 'hello world'
print(str.find('world'))

