import datetime
from datetime import  datetime

start = datetime.now()
###############################
import math

def isPrime(n):
    for i in range(2, int((n*0.5)+1)):
        # print(i)
        if (n % i) == 0:
            # print(f'Finished in {i} loop')
            return  False

    return True

itr = 2
cnt = 0
while True:

    if isPrime(itr):
        cnt += 1
        if cnt == 10001:
            break
        # print(itr)
    itr += 1

print(itr)

###############################
end = datetime.now()
print(f"Time taken: {(end - start).total_seconds()}")
