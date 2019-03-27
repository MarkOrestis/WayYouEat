import collections

def subset_sum_count(lst, a, b):
    sum_counts = collections.Counter({0: 1})
    for x in lst:
        for s, c in list(sum_counts.items()):
            sum_counts[s + x] += c
    return sum(c for (s, c) in sum_counts.items() if a <= s <= b)

arr = [3, 4, 12, 10, 8, 5, 9, 18, 20, 14, 1, 1, 2, 1]
n = 12
m = 12
print(subset_sum_count(arr, n, m))