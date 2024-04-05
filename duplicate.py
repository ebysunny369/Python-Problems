my_list = [1, 2, 3, 4, 4, 5, 6, 6]
duplicates = []
for item in my_list:
    if my_list.count(item) > 1 and item not in duplicates:
        duplicates.append(item)
print("Duplicates:", duplicates)
