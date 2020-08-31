# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minValueKey(self,root):
        current = root
        while(current.left is not None):
            current = current.left
        
        return current
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None :
            return root
        
        elif(key < root.val):
            root.left = self.deleteNode(root.left, key)
        
        elif(key > root.val):
            root.right = self.deleteNode(root.right,key)
        
        else:
            if(root.right is None):
                temp = root.left
                root = None
                return temp
            elif(root.left is None):
                temp = root.right
                root = None
                return temp
            else:
                temp = self.minValueKey(root.right)
                root.val = temp.val
                root.right = self.deleteNode(root.right,temp.val)
            
        
        return root