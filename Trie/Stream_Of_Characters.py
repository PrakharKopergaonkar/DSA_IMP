class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class Trie:
    def __init__(self):
        self.rootNode = TrieNode()
    
    def getRootNode(self):
        return self.rootNode
    
    def addword(self,word):
        currNode = self.rootNode
        for i in range(len(word)-1,-1,-1):
            if(word[i] not in currNode.children):
                currNode.children[word[i]] = TrieNode()
            currNode = currNode.children[word[i]]
        currNode.endOfWord = True

        
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            self.trie.addword(word)
        self.queryword = ""

    def query(self, letter: str) -> bool:
        self.queryword += letter
        Node = self.trie.getRootNode()
        for letter in reversed(self.queryword):
            if(letter not in Node.children):
                break
            
            Node = Node.children[letter]
            
            if(Node.endOfWord):
                return True
        
        return False
        
        
        
    
    
        
    


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)