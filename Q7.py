n = int(input("Enter n: ")) 
r = int(input("Enter r: ")) 

fact_n = 1
for i in range(1, n + 1):
    fact_n *= i

fact_n_r = 1
for i in range(1, n - r + 1):
    fact_n_r *= i

fact_r = 1
for i in range(1, r + 1):
    fact_r *= i

nPr = fact_n // fact_n_r

nCr = fact_n // (fact_r * fact_n_r)

print("nPr (Permutation):", nPr)
print("nCr (Combination):", nCr)
