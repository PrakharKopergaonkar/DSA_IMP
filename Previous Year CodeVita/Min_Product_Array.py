n, k = map(int, input().split(' '))

a1 = list(map(int, input().split(' ')))
a2 = list(map(int, input().split(' ')))

multiply = 0

for i in range(0,n):
    multiply+=(a1[i]*a2[i])
    print(a1[i]*a2[i])
multiply_org = multiply
for i in range(0,n):
    multiply = min(multiply, multiply_org - (a1[i]*a2[i]) + (a1[i]-2*k)*a2[i], multiply_org - (a1[i]*a2[i]) + (a1[i]+2*k)*a2[i])

print(multiply)

