#   Created by Roshan Jayswal 
#   Copyright © 2021 AppMillers. All rights reserved.

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False
        self.words = list()
        self.n = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insertString(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch:node})
            current = node
            if node.n < 3:
                node.words.append(word)
                node.n += 1
        current.endOfString = True
        print("Successfully inserted")
    
    def searchString(self, word):
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)
            if node == None:
                return False
            currentNode = node

        if currentNode.endOfString == True:
            return True
        else:
            return False
        
    def find_word_by_prefix(self, c):
        if self.root and c in self.root.children:
            self.root = self.root.children[c]
            return self.root.words
        else:
            self.root = None
            return []

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        newTrie = Trie()
        for word in products:
            newTrie.insertString(word)
        return [newTrie.find_word_by_prefix(c) for c in searchWord]       

def deleteString(root, word, index):
    ch = word[index]
    currentNode = root.children.get(ch)
    canThisNodeBeDeleted = False

    if len(currentNode.children) > 1:
        deleteString(currentNode, word, index+1)
        return False
    
    if index == len(word) - 1:
        if len(currentNode.children) >= 1:
            currentNode.endOfString = False
            return False
        else:
            root.children.pop(ch)
            return True
    
    if currentNode.endOfString == True:
        deleteString(currentNode, word, index+1)
        return False

    canThisNodeBeDeleted = deleteString(currentNode, word, index+1)
    if canThisNodeBeDeleted == True:
        root.children.pop(ch)
        return True
    else:
        return False



""" 
newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("Appl")
deleteString(newTrie.root, "App", 0)
print(newTrie.searchString("App"))
"""
sol = Solution()
products = ['mousepad', 'moneypot', 'monitor', 'mouse', 'mobile']
print(sol.suggestedProducts(products, "mouse"))


"""[Method 2]
"""
class TrieNode:
    def __init__(self):
        # Stores children nodes and whether node is the end of a word
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        # Insert character by character into trie
        for c in word:
            # if character path does not exist, create it
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True
        

    def search(self, word: str) -> bool:
        cur = self.root
        # Search character by character in trie
        for c in word:
            # if character path does not exist, return False
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        # Same as search, except there is no isEnd condition at final return
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True    