# ============================================================
#   PYTHON LISTS — Intermediate Codes
#   All 7 problems in one file with full comments
# ============================================================


# ────────────────────────────────────────────────────────────
# 01 — Remove Duplicates (keep original order)
# ────────────────────────────────────────────────────────────
# Problem: Remove repeated values but keep the order intact.
# Trick: Use a set to track what we've already seen.

def remove_dupes(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            result.append(x)
            seen.add(x)
    return result

print("01 - Remove Duplicates:")
print(remove_dupes([1, 2, 2, 3, 1, 4, 4, 5]))
# Output: [1, 2, 3, 4, 5]
print()


# ────────────────────────────────────────────────────────────
# 02 — Flatten a Nested List
# ────────────────────────────────────────────────────────────
# Problem: Convert [[1,[2,3]],[4]] into [1,2,3,4].
# Trick: Use recursion — if item is a list, go deeper.

def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):      # if it's a list, go inside it
            result.extend(flatten(item))  # recursively flatten it
        else:
            result.append(item)          # normal value, just add it
    return result

print("02 - Flatten Nested List:")
print(flatten([1, [2, [3, 4]], [5, 6], 7]))
# Output: [1, 2, 3, 4, 5, 6, 7]
print()


# ────────────────────────────────────────────────────────────
# 03 — Rotate List by k Steps (Left Rotation)
# ────────────────────────────────────────────────────────────
# Problem: Shift elements left by k positions.
# Example: [1,2,3,4,5] rotated by 2 → [3,4,5,1,2]
# Trick: Slice at k and swap the two halves.

def rotate(lst, k):
    k = k % len(lst)          # handle k > length
    return lst[k:] + lst[:k]  # cut at k and rejoin

print("03 - Rotate List:")
print(rotate([1, 2, 3, 4, 5], 2))   # [3, 4, 5, 1, 2]
print(rotate([1, 2, 3, 4, 5], 7))   # same as k=2 since 7%5=2
print()


# ────────────────────────────────────────────────────────────
# 04 — Find Second Largest Number
# ────────────────────────────────────────────────────────────
# Problem: Find the 2nd biggest value without using sorted twice.
# Trick: Convert to set (removes duplicates), sort descending,
#        then just pick index [1].

def second_largest(lst):
    unique = sorted(set(lst), reverse=True)  # sorted unique values
    if len(unique) >= 2:
        return unique[1]
    return None   # not enough unique values

print("04 - Second Largest:")
print(second_largest([10, 20, 4, 45, 99]))   # 45
print(second_largest([5, 5, 5]))             # None (all same)
print()


# ────────────────────────────────────────────────────────────
# 05 — Chunk List into Groups of Size n
# ────────────────────────────────────────────────────────────
# Problem: Split [1,2,3,4,5,6,7] into groups of 3
#          → [[1,2,3], [4,5,6], [7]]
# Trick: Use range with step = size, slice each group.

def chunk(lst, size):
    return [lst[i : i + size] for i in range(0, len(lst), size)]
    # range(0, 7, 3) gives us: 0, 3, 6
    # lst[0:3], lst[3:6], lst[6:9]

print("05 - Chunk List:")
print(chunk([1, 2, 3, 4, 5, 6, 7], 3))   # [[1,2,3], [4,5,6], [7]]
print(chunk([1, 2, 3, 4, 5, 6], 2))      # [[1,2], [3,4], [5,6]]
print()


# ────────────────────────────────────────────────────────────
# 06 — Matrix Transpose
# ────────────────────────────────────────────────────────────
# Problem: Flip rows and columns of a 2D list.
# Example:
#   Input:   [[1,2,3],      Output:  [[1,4,7],
#             [4,5,6],               [2,5,8],
#             [7,8,9]]               [3,6,9]]
# Trick: zip(*matrix) unpacks and zips rows together.

def transpose(matrix):
    return [list(row) for row in zip(*matrix)]
    # zip(*matrix) → pairs up columns across all rows

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("06 - Matrix Transpose:")
for row in transpose(matrix):
    print(row)
# [1, 4, 7]
# [2, 5, 8]
# [3, 6, 9]
print()


# ────────────────────────────────────────────────────────────
# 07 — Intersection of Two Lists
# ────────────────────────────────────────────────────────────
# Problem: Find common elements between two lists.
# Trick: Convert both to sets and use & (AND) operator.

def intersect(a, b):
    return list(set(a) & set(b))   # & gives common elements only

print("07 - Intersection:")
print(intersect([1, 2, 3, 4], [3, 4, 5, 6]))      # [3, 4]
print(intersect([10, 20, 30], [20, 30, 40, 50]))   # [20, 30]
print()


# ============================================================
#   BONUS — All topics in one place for quick revision
# ============================================================
# 01  remove_dupes  → set for tracking seen values
# 02  flatten       → recursion + isinstance check
# 03  rotate        → slicing  lst[k:] + lst[:k]
# 04  second_largest→ set + sorted + index [1]
# 05  chunk         → list comp + range(0, n, size)
# 06  transpose     → zip(*matrix)
# 07  intersect     → set(a) & set(b)
# ============================================================