#%%
def valid_string(s):
    for ch in s:
        if not (ch.isalpha() or ch.isdigit()):
            return False
    return True
t = input("Enter a string: ")
if valid_string(t):
    print("Valid string: contains only the Alphabet and digits (0-9).")
else:
    print("Invalid string: contains characters other than the Alphabet and the digits.")
    

