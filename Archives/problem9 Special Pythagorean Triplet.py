"""
First generate the triplets
"""

range_limit = 1000
triplets = []

for i in range(1,range_limit+1):
    a = i
    print(f"a is: {a}")
    b_start_value = i + 1
    for j in range(i+1, range_limit):
        b = j
        c = range_limit - (a + b)
        if c < b or c ==b:
            break
        triplets.append([a,b,c])
        print(f"b is: {b}")
        print(f"c is: {c}")

        print("\n")
    print("\n\n")

print(triplets)

"""
Finding the product of the triplets 
"""
mult = 1
for i in triplets:
    if i[0]**2 + i[1]**2 == i[2]**2:
        print("Pythagorean")
        print(f"triplets is: {i}")
        mult = i[0] * i[1] * i[2]
        print(f"mult is: {mult}")
