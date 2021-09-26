import datetime
from datetime import  datetime

start = datetime.now()
###############################
sumOfSquares = 0
sumOfNumber = 0
for i in range(1,101,1):
    sumOfSquares += (i*i)
    sumOfNumber += i

diff = (sumOfNumber ** 2) - sumOfSquares

print(diff)
###############################
end = datetime.now()
print(f"Time taken: {(end - start).total_seconds()}")
