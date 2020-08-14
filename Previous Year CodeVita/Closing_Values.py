from collections import defaultdict
N = int(input())

trades = []
for i in range(0,N):
    data = defaultdict(str)
    data['ID'], data['Type'], data['Name'], data['Price'],data['Quantity'] = input().split(' ')
    trades.append(data)

sell =defaultdict(list)
buy = defaultdict(list)

for i in range(0,len(trades)):
    if(trades[i]['Type']=='Sell'):
        sell[trades[i]['Name']] = [int(trades[i]['Price']),int(trades[i]['Quantity'])]
    elif(trades[i]['Type']=='Buy'):
        buy[trades[i]['Name']].append([int(trades[i]['Price']),int(trades[i]['Quantity'])])

flag = False
for key,value_sell in sell.items():
    for value_buy in buy[key]:
        if(value_buy[0]>=value_sell[0]):
            flag = True
            print(str(key)+":"+str(value_sell[0])) 
            break
if(not flag):
    print("Stocks not traded")