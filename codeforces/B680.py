_, origin = list(map(int, input().split(' ')))
cities = list(map(int, input().split(' ')))
origin -= 1
i, criminals = 1, cities[origin]

while True:
    if origin+i < len(cities) and origin-i >= 0:
        criminals += 2 if cities[origin+i] == cities[origin-i] == 1 else 0
    elif origin+i < len(cities):
        criminals += cities[origin+i]
    elif origin >= i:
        criminals += cities[origin-i]
    else: break
    i+=1
print(criminals)