a = int(input())
b = int(input())

# b의 첫째자리와 a의 곱
print(a * (b % 10))
# b의 둘째자리와 a의 곱
t = (b % 100) // 10 
print(a * t)
# b의 셋째자리와 a의 곱
print(a * (b // 100))
# b와 a의 곱
print(a * b)