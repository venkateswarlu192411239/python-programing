from collections import Counter

arr = [1, 2, 3, 2, 4, 5, 6, 1, 7, 8, 5]

count = Counter(arr)
duplicates = [item for item, freq in count.items() if freq > 1]

print("Duplicates:", duplicates)
