import datetime
from datetime import  datetime

start = datetime.now()
maxPalindrome = 0
for i in range(999,100,-1):
    for j in range(i,100,-1):
        currentProduct = i * j
        if maxPalindrome < currentProduct and str(currentProduct) == str(currentProduct)[::-1]:
            maxPalindrome = currentProduct

print(maxPalindrome)


end = datetime.now()
print(f"Time taken: {(end - start).total_seconds()}")
