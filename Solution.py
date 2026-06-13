def sum_negatives_between_min_max(arr):
    if not arr:
        return 0
    min_idx = arr.index(min(arr))
    max_idx = arr.index(max(arr))
    left = min(min_idx, max_idx)
    right = max(min_idx, max_idx)
    if right - left <= 1:
        return 0
    middle = arr[left + 1:right]
    return sum(x for x in middle if x < 0)


if __name__ == "__main__":
    examples = [
        [10, -1, -2, -3, 0, -4, -5],
        [-1, 5, -2, 10, -3],
        [3, -5, 0, -2, 10, -7, 1, -3, 8],
    ]
    for arr in examples:
        print(f"{arr} -> {sum_negatives_between_min_max(arr)}")
