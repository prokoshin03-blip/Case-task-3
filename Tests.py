from solution import sum_negatives_between_min_max

assert sum_negatives_between_min_max([]) == 0
assert sum_negatives_between_min_max([10, -5]) == 0
assert sum_negatives_between_min_max([10, 1, 2, 3, -1]) == 0
assert sum_negatives_between_min_max([10, -1, -2, -3, 0, -4, -5]) == -10
assert sum_negatives_between_min_max([-1, 5, -2, 10, -3]) == -2

print("Все тесты пройдены!")
