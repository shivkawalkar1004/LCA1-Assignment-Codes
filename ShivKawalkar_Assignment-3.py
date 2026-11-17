#%%
def m(a, b, c):
    sides = sorted([a, b, c])
    x, y, z = sides
    return (x**2 + y**2) == z**2
p = int(input("Enter first side: "))
q = int(input("Enter second side: "))
r = int(input("Enter third side: "))
if m(p, q, r):
    print("The triangle is a right-angled triangle with hypotenuse:", max(p, q, r))
else:
    print("The triangle is not a right-angled triangle.")
    
# %%
 