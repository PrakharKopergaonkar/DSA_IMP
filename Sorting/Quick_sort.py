from random import randint
#randomized pivot function is used to avoid worst case scenario - i.e totally unbalanced partition 
def randomized_pivot(arr,start,end):
    pivot = randint(start,end)
    arr[end],arr[pivot] = arr[pivot],arr[end]
    return partition(arr,start,end)
def partition(arr, start,end):
    pivot = arr[end]
    pIndex = start
    for i in range(start,end):
        if(arr[i]<=pivot):
            arr[i],arr[pIndex] = arr[pIndex], arr[i]
            pIndex+=1
    arr[pIndex],arr[end] = arr[end], arr[pIndex]
    return pIndex
def quick_sort(arr,start,end):
    if(start>=end):
        return
    pindex = randomized_pivot(arr,start,end)
    quick_sort(arr,start,pindex-1)
    quick_sort(arr,pindex+1,end)
arr = [7,2,1,6,8,5,3,4]
quick_sort(arr,0,len(arr)-1)
print(arr)