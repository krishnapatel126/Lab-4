s = input("Enter a string: ") 
count = 0 
digit_count = 0 
for char in s: 
    if ('A' <= char <= 'Z') or ('a' <= char <= 'z'): 
        count += 1 
    elif '0' <= char <= '9': 
        digit_count += 1 
print("Number of alphabets:",count) 
print("Number of digits:", digit_count) 
