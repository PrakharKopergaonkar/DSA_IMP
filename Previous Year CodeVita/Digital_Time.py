def generate_maxTime(arr_list,time,point):
    upper_limit = 0
    if(point==6):
        return True
    if(point==0):
        upper_limit = 2
    elif(point==1 and time[point-1]<2):
        upper_limit = 9
    elif(point == 1 and time[point-1]==2):
        upper_limit = 4
    
    elif(point>1 and time[1]==4 and time[0]==2):
        upper_limit = 0
    elif(point==2 or point==4):
        upper_limit = 5
    elif((point==3 or point==5)):
        upper_limit=9
    

    for i in range(upper_limit,-1,-1):
        if(arr_list[i]>0):
            time[point] = i
            arr_list[i]-=1
            if(generate_maxTime(arr_list,time,point+1)):
                return True
            time[point] = 0
            arr_list[i]+=1
    return False
arr = list(map(int, input().split(',')))

arr_list = [0 for i in range(0,10)]

for i in arr:
    arr_list[i] += 1
time = [0 for i in range(0,6)]

if(generate_maxTime(arr_list,time,0)): 
    for i in range(0,len(time)):
        print(time[i],end="")
        if(i==1 or i==3):
            print(":",end="")
else:
    print("Impossible")
