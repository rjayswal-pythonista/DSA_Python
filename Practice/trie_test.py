from typing import List

class TrieNode:
    def __init__(self):
        self.childrens = {}
        self.endOfStrings = False
        self.words = list()
        self.n = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insertNode(self, word):
        current = self.root        
        for i in word:
            ch = i
            node = current.childrens.get(ch)
            if node == None:
                node  = TrieNode()
                current.childrens.update({ch:node})
            current = node
            if current.n < 3:
                current.words.append(word)
                current.n +=1
        current.endOfStrings = True
        print("Insert Successful")
    
    def search(self, word):
        current = self.root
        for i in word:
            node = current.childrens.get(i)
            if node == None:
                return False
            current = node
        if current.endOfStrings:
            return True
        else:
            return False 
        
    def find_word_by_prefix(self, c):
        if self.root and c in self.root.childrens:
            self.root = self.root.childrens[c]
            return self.root.words
        else:
            self.root = None
            return []

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        newTrie = Trie()
        for word in products:
            newTrie.insertNode(word)
        return [newTrie.find_word_by_prefix(c) for c in searchWord]
"""         
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        list_ = []
        products.sort()
        for i, c in enumerate(searchWord):
            products = [ p for p in products if len(p) > i and p[i] == c ]
            list_.append(products[:3])
        return list_
"""

sol = Solution()
products = ['mousepad', 'moneypot', 'monitor', 'mouse', 'mobile']
print(sol.suggestedProducts(products, "mouse"))

