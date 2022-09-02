distance = [1,2,3,5]

for i in distance:
    print(i)

a = distance[0]
for item in distance:
    if item < a:
        a = item
print(a)
