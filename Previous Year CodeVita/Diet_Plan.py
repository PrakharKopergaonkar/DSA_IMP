max_nutrients = input().split(' ') #P C F
items = [i.split(' ') for i in input().split('|')]

for i in range(0,len(max_nutrients)):
    max_nutrients[i] = int(max_nutrients[i][:len(max_nutrients)])

for i in range(0,len(items)):
    for j in range(0,len(items[i])):
        items[i][j] = int(items[i][j][:-1])

items.sort(key=lambda x: sum(x),reverse=True)

while(len(items)):
    curr_item = items.pop(0)
    if(curr_item[0]<=max_nutrients[0] and curr_item[1]<=max_nutrients[1] and curr_item[2]<=max_nutrients[2]):
        max_nutrients[0]-=curr_item[0]
        max_nutrients[1]-=curr_item[1]
        max_nutrients[2]-=curr_item[2]
        items.append(curr_item)

print(max_nutrients[0], max_nutrients[1], max_nutrients[2])