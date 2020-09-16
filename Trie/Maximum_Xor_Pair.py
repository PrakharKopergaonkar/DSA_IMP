#Build a Trie which store binary 32-bit representaion of every number
#Store all values in the trie
#For each number find the number that can form max xor pair
#return max among all found in previous step
#Time complexity O(nlog(maxofnumbers))
import sys
class TrieNode :
    def __init__(self):
        self.left = None
        self.right = None

class Trie:
    def __init__(self):
        self.head = TrieNode()
    
    def insert(self,n):
        curr = self.head
        for i in range(31,-1,-1):
            b = (n>>i)&1
            if(b==0 and curr.left!=None):
                curr=curr.left
            elif(b==0 and curr.left==None):
                curr.left = TrieNode()
                curr = curr.left
            elif(b==1 and curr.right!=None):
                curr = curr.right
            else:
                curr.right = TrieNode()
                curr = curr.right
    
    def findXorPair(self,nums):
        max_xor = -sys.maxsize
        for num in nums:
            curr = self.head
            curr_xor = 0
            for i in range(31,-1,-1):
                b = (num>>i)&1
                if(b==0 and curr.right!=None):
                    curr = curr.right
                    curr_xor += 2**i
                elif(b==0 and curr.right==None):
                    curr = curr.left
                    
                elif(b==1 and curr.left!=None):
                    curr = curr.left
                    curr_xor += 2**i
                else:
                    curr = curr.right
            max_xor = max(max_xor, curr_xor)
        
        
        return max_xor if(max_xor!=-sys.maxsize) else 0
                    
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        a = Trie()
        for n in nums:
            a.insert(n)
        
        return a.findXorPair(nums)
        
        