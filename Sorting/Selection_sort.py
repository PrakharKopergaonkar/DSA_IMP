def selection_sort(arr):
    n = len(arr)
    for i in range(0,n):
        min_idx = i
        for j in range(i+1,n):
            if(arr[j]<arr[min_idx]):
                min_idx = j
        
        arr[i],arr[min_idx] = arr[min_idx],arr[i]
arr = [2,4,5,1]
selection_sort(arr)
print(arr)