'''
Reference for detailed algorithm https://math.stackexchange.com/a/389697
'''

def isPrime(n):
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return  True

largestPrimeFactor = 2
number = 600851475143
iterator = 2
count = 0
while iterator <= number:
    if isPrime(iterator) and number % iterator == 0:
        # print(f"{iterator} is Prime")
        largestPrimeFactor = iterator
        number = number / iterator
        iterator = 2
    else:
        iterator += 1
    count += 1

print(largestPrimeFactor)
print(f"Finished in {count} loops")
