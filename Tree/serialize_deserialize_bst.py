# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        output_string = []
        def dfs(root):
            if(root==None):
                output_string.append("*")
            else:
                output_string.append(str(root.val))
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        return ",".join(i for i in output_string)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        self.data = data.split(',')
        def helper():
            val = self.data.pop(0)
            if(val=="*"):
                return None
            root = TreeNode(int(val))
            root.left = helper()
            root.right = helper()
            return root
        
        return helper()