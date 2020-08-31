#Leet Code Link - https://leetcode.com/problems/largest-component-size-by-common-factor/
#The question basically asks for length of maximum size subgraph in a disconnected graph
# Naive solution would be using BFS or DFS. It causes TLE 
# Efficient Solution is using Union and find algorithm
# In this we first count primes set (defaultdict(list)) that store indexes it divide
# For example for [4,6,15,35] prime_set would be {2:[0,1],3:[1,2],5:[2,3],7:[3]}
# The for each list we peform union operation
# At the end We find parent for each number and using counter return frequency of max frequent parent  

import math
from collections import defaultdict, Counter
class Unf:
    def __init__(self,n):
        self.p = list(range(n))
    
    def find(self,x):
        if(self.p[x]!=x):
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    def union(self,x,y):
        x_parent, y_parent = self.find(x), self.find(y)
        self.p[x_parent] = y_parent
class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        def primeFactors(n):
            prime_set = set()
            while n % 2 == 0: 
                prime_set.add(2)
                n = n // 2
            for i in range(3,int(math.sqrt(n))+1,2): 
                while n % i== 0: 
                    prime_set.add(i)
                    n = n // i
            if n > 2: 
                prime_set.add(n)
            return prime_set
        
        UF = Unf(len(A))
        primes = defaultdict(list)
        for i in range(0,len(A)):
            all_primes = primeFactors(A[i])
            for j in all_primes:
                primes[j].append(i)
        
        for key, value in primes.items():
            for i in range(0,len(value)-1):
                UF.union(value[i],value[i+1])
        
        a = max(Counter([UF.find(i) for i in range(0,len(A))]).values())
        return a
        
        