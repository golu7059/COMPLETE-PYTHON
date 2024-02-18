# Creating tuples
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('a', 'b', 'c', 'd', 'e')

# Accessing elements of a tuple
print("First element of tuple1:", tuple1[0])
print("Last element of tuple2:", tuple2[-1])

# Slicing tuples
print("Sliced tuple1:", tuple1[1:4])
print("Sliced tuple2:", tuple2[:-2])

# Concatenating tuples
tuple3 = tuple1 + tuple2
print("Concatenated tuple:", tuple3)

# Tuple length
print("Length of tuple3:", len(tuple3))

# Count occurrences of an element in a tuple
print("Count of 'a' in tuple3:", tuple3.count('a'))

# Index of the first occurrence of an element in a tuple
print("Index of 'b' in tuple3:", tuple3.index('b'))

# Unpacking tuples
a, b, c = (10, 20, 30)
print("Unpacked values:", a, b, c)

# Iterating over tuples
print("Iterating over tuple1:")
for item in tuple1:
    print(item)

# Checking membership in a tuple
print("Is 'c' in tuple2?", 'c' in tuple2)

# Tuple immutability
# tuple1[0] = 100  # This will raise an error since tuples are immutable

# Nested tuples
nested_tuple = ((1, 2, 3), ('a', 'b', 'c'))
print("Nested tuple:", nested_tuple)

# Accessing elements of nested tuples
print("Element at (0, 1) in nested tuple:", nested_tuple[0][1])

# Tuple packing
packed_tuple = 1, 2, 3
print("Packed tuple:", packed_tuple)

# Tuple unpacking
x, y, z = packed_tuple
print("Unpacked values:", x, y, z)
