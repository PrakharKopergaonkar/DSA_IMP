import heapq
class MaxHeap:
    def __init__(self):
        self.data = []
    
    def getarr(self):
        return [-i for i in self.data]
    

    def push(self, val):
        heapq.heappush(self.data, -val)
    
    def heapify(self,arr):
        for i in arr:
            self.push(i)

    def pop(self):
        return -heapq.heappop(self.data)
heap_arr = MaxHeap()

N, K = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))
heap_arr.heapify(arr)

while(K>0):
    n = heap_arr.pop()
    n = n//2
    heap_arr.push(n)
    K-=1
print(sum(heap_arr.getarr()))