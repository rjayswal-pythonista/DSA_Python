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