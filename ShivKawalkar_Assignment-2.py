#%%
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    l = a
elif b >= a and b >= c:
    l = b
elif c >= a and c >= b:
    l = c
else:
    print("Invalid input")
print("The largest number is:", l)


# %%
