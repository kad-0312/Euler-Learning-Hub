# Creating a list
numbers_list = [1, 2, 3, 4, 5]
print("List:", numbers_list)

# Accessing elements
print("First element:", numbers_list[0])

# Inserting elements
numbers_list.insert(2, 99)
print("After insertion:", numbers_list)

# Deleting elements
numbers_list.remove(99)
print("After deletion:", numbers_list)

# Updating elements
numbers_list[0] = 100
print("After updating:", numbers_list)

# Traversing the list
print("Traversing the list:")
for num in numbers_list:
    print(num, end=" ")
print()
