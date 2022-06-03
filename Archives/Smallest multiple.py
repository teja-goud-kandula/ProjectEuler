'''
Further reference : https://www.geeksforgeeks.org/smallest-number-divisible-first-n-numbers/
'''

def factorial_list(num):
    factors = []
    i = 2
    while(num !=1 ):
        if num % i == 0:
            factors.append(i)
            num = num / i
            i = 2
        else:
            i += 1

    return factors

lcm = 1
for x in range(2, 21):
    factors = factorial_list(x)
    to_multiply_factors = []
    temp = lcm
    for i in factors:
        if temp % i == 0:
            temp = temp / i
        else:
            to_multiply_factors.append(i)

    for i in to_multiply_factors:
        lcm = lcm * i

print(lcm)
