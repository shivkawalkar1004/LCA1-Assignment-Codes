#%%
##---------- 1. LIST of students ----------
students_list = ["Shiv", "Sammit", "Soham"]
print("Original List:", students_list)
# Add
students_list.append("Chinmay")
print("After Add:", students_list)
# Update 
students_list[1] = "Siddhesh"
print("After Update:", students_list)
# Delete
students_list.remove("Soham")
print("After Deletion:", students_list)


# ---------- 2. TUPLE of students ----------
students_tuple = ("Shiv", "Sammit", "Soham")
print("\nOriginal Tuple:", students_tuple)
# Add
temp = list(students_tuple)
temp.append("Chinmay")
students_tuple = tuple(temp)
print("After Add:", students_tuple)
# Update
temp = list(students_tuple)
temp[1] = "Siddhesh"
students_tuple = tuple(temp)
print("After Update:", students_tuple)
# Delete
temp = list(students_tuple)
temp.remove("Shiv")
students_tuple = tuple(temp)
print("After Delete:", students_tuple)

# ---------- 3. DICTIONARY of students ----------
students_dict = {
    1: "Shiv",
    2: "Sammit",
    3: "Soham"
}
print("\nOriginal Dictionary:", students_dict)
# Add
students_dict[4] = "Chinmay"
print("After Add:", students_dict)
# Update
students_dict[2] = "Siddhesh"
print("After Update:", students_dict)
# Delete
del students_dict[3]
print("After Delete:", students_dict)