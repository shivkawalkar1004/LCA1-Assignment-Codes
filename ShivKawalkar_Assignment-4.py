#%%
import numpy as np
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
a = []
b = []
print("\nEnter elements for Matrix 1:")
for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"Element [{i}][{j}]: "))
        row.append(value)
    a.append(row)
print("\nEnter elements for Matrix 2:")
for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"Element [{i}][{j}]: "))
        row.append(value)
    b.append(row)
p = np.array(a)
q = np.array(b)
r = p + q
print("\nMatrix 1:\n", p)
print("Matrix 2:\n", q)
print("Sum of Matrices:\n", r)

