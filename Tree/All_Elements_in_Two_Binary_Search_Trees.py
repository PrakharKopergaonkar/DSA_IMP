# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.list1 = []
        self.list2 = []
    def dfs(self,root,typeRoot):
        if(root==None):
            return
        self.dfs(root.left,typeRoot)
        if(typeRoot==1):
            self.list1.append(root.val)
        else:
            self.list2.append(root.val)
        self.dfs(root.right,typeRoot)
        
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.dfs(root1,1)
        self.dfs(root2,2)
        i, j = 0, 0
        output_list = []
        while(i<len(self.list1) or j < len(self.list2)):
            if(i<len(self.list1) and j < len(self.list2)):
                if(self.list1[i]<self.list2[j]):
                    output_list.append(self.list1[i])
                    i+=1
                else:
                    output_list.append(self.list2[j])
                    j+=1
            elif(i<len(self.list1)):
                output_list.append(self.list1[i])
                i+=1
            elif(j<len(self.list2)):
                output_list.append(self.list2[j])
                j+=1
        
        return output_list