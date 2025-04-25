N = int(input("Enter the number of Fibonacci terms: ")) 
a = 0 
b = 1 
print("Fibonacci Series:", end=" ") 
for i in range(N): 
    print(a, end=" ") 
    temp = a + b 
    a = b 
    b = temp 
