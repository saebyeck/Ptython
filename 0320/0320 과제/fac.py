num = int(input("Enter a number: "))
fact = 1
factor_str = ""  

for i in range(num, 0, -1):
    fact *= i
    if i != 1:
        factor_str += str(i) + "*"
    else:
        factor_str += str(i)

print(f"{factor_str} = {fact}")