# 🚀 Intermediate Python Series

This repository contains intermediate-level Python problems with clean, well-commented solutions.

## 📌 Topics Covered
- List manipulation (rotation, chunking, duplicates)
- Recursion (flatten nested list)
- Matrix operations (transpose using zip)
- Set operations (intersection)

## 🧠 What I Learned
- Writing Pythonic code using slicing and built-ins
- Optimizing time complexity using sets
- Breaking complex problems using recursion

## 💻 Example

```python
def rotate(lst, k):
    k = k % len(lst)
    return lst[k:] + lst[:k]
