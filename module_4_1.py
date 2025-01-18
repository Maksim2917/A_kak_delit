from fake_math import divide as fake_divide

from true_math import divide as truth_divide

result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = truth_divide(49, 7)
result4 = truth_divide(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)