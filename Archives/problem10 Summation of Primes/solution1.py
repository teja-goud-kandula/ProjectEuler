from datetime import datetime

range_limit = 2000000
# range_limit = 10

def is_prime(num):
    # skipping this step because until 10 I have accounted the sum of the prime numbers
    # if num == 2 or num == 3 or num == 5 or num == 7:
    #     return True
    half = int(num/2)+1
    # print(f"half is: {half}")
    i = 3
    while num%i != 0:
        i = i + 2
        if i >= half:
            return True
    # print(f"i is {i}")
    return False

start_time = datetime.now()


sum_of_primes = 17 # sum of prime numbers until 10
for iterator in range(11,range_limit+1,2):
    print(f"iterator is: {iterator}")
    if is_prime(iterator):
        sum_of_primes = sum_of_primes + iterator
print(sum_of_primes)


end_time = datetime.now()
print(f"start time: {start_time}")
print(f"end time: {end_time}")
print(end_time - start_time)
