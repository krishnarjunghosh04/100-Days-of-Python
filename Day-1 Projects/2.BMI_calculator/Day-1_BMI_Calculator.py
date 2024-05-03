# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# calculation
new_height = float(height)
new_weight = int(weight)
bmi = int(new_weight/(new_height*new_height))
# print bmi
print(bmi)