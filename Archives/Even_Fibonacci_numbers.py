n1 = 1
n2 = 2
n3 = 0
sum = 2
# print(n1)
# print(n2)
while True:
    n3 = n1 + n2
    if n3 > 4000000:
        break
    if n3 % 2 == 0:
        sum += n3
        # print(f"n3 value is : {n3}")
        # print(f"Sum value is : {sum}")
    n1 = n2
    n2 = n3
    #print(n3)

print(sum)
