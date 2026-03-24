"""
🟡 LISTS - 7 Python Intermediate Examples (08-14)
List manipulation including sorting, filtering, flattening, and transformations
"""

# 08 — Remove Duplicates (keep order)
def remove_dupes(lst):
    """Remove duplicates from list while preserving order"""
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

print(remove_dupes([1, 2, 2, 3, 1, 4]))  # [1, 2, 3, 4]


# 09 — Flatten Nested List
def flatten(lst):
    """Recursively flatten nested lists into a single list"""
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print(flatten([1, [2, [3, 4]], [5, 6]]))  # [1, 2, 3, 4, 5, 6]


# 10 — Rotate List by k Steps
def rotate(lst, k):
    """Rotate list k positions to the right"""
    k = k % len(lst)
    return lst[k:] + lst[:k]

print(rotate([1, 2, 3, 4, 5], 2))  # [3, 4, 5, 1, 2]


# 11 — Find Second Largest
def second_largest(lst):
    """Find the second largest element in list"""
    unique = sorted(set(lst), reverse=True)
    return unique[1] if len(unique) >= 2 else None

print(second_largest([10, 20, 4, 45, 99]))  # 45


# 12 — Chunk List into Groups
def chunk(lst, size):
    """Split list into chunks of given size"""
    return [lst[i:i+size] for i in range(0, len(lst), size)]

print(chunk([1,2,3,4,5,6,7], 3))  # [[1,2,3], [4,5,6], [7]]


# 13 — Matrix Transpose
def transpose(matrix):
    """Transpose a 2D matrix"""
    return [list(row) for row in zip(*matrix)]

m = [[1,2,3],[4,5,6],[7,8,9]]
for row in transpose(m):
    print(row)
# [1, 4, 7]
# [2, 5, 8]
# [3, 6, 9]


# 14 — Intersection of Two Lists
def intersect(a, b):
    """Find common elements between two lists"""
    return list(set(a) & set(b))

print(intersect([1,2,3,4], [3,4,5,6]))  # [3, 4]
