
"""
    Read files and return combined elements
"""

with open("file1.txt") as fl_1:
    fl_1 = fl_1.readlines()
    list_1 = [num.strip() for num in fl_1]


with open("file2.txt") as fl_2:
    fl_2 = fl_2.readlines()
    list_2 = [num.strip() for num in fl_2]


print(list_1)
print(list_2)

# Combining Data using list comprehension
combined = list(set([int(n) for n in list_2 if n in list_1]))
print(combined)


