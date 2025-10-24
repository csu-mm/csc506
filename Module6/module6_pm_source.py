# MS - Artificial Intelligence and Machine Learning
# Course: CSC506 - Design and Analysis of Algorithms
# Professor: Dr. Jonathan Vanover
# Module 6: Portfolio Milestone
# Created by Mukul Mondal
# Saturday, October 19, 2025
#
# Python Program:
#

'''
Problem statement:

Analysis and Optimization

Analyze the empirical data to determine time and space complexity trends.
Compare algorithm performances and identify strengths and weaknesses.
Implement any necessary optimizations or improvements to the algorithms.
Prepare a report summarizing the analysis and optimizations undertaken.

I chose:
BST creation, Search Algorithm 
-- Create BSTs with different empirical data
-- Analyze Search Algorithm performance on the BST.
-- If needed, update BST creation Algorithm
'''

import numpy as np
from numpy.core.fromnumeric import sort
from os import system, name



# This is just a helper function to clear the screen
# This is not required, per problem statement.
def clearScreen():
    if name == 'nt':  # For windows system
        _ = system('cls')    
    else:             # for non-windows system
        _ = system('clear')
    print("")
    return


# BST Node
class Node:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

# BST
class BST:
    def __init__(self):
        self.root = None
        self.comparisonCount: int = 0

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key)
        return node

    # search a key in the BST    
    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None:
            return node
        
        self.comparisonCount += 1
        if node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)


class BalancedTree:
    def __init__(self):
        self.Root: Node = None
        self.comparisonCount: int = 0

    def search(self, key):
        return self._search_recursive(self.Root, key)

    def _search_recursive(self, node, key):
        if node is None:
            return node
        self.comparisonCount += 1
        if node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)


def build_balanced_bst(arr):
    if not arr:
        return None

    mid = len(arr) // 2
    root = Node(arr[mid])
    root.left = build_balanced_bst(arr[:mid])
    root.right = build_balanced_bst(arr[mid+1:])
    return root



# Main test function
# Executes Algorithms
def run_tests():
    """
    Runs algorithms on different inputs.
    Runs algorithms on BST and Balanced BST
    Runs 'search item' and records how many times comparison operation executed
        
    Parameters
    ----------
    None

    Return : None, shows output
    ----------    
    """

    searchItem: int = 0
    
    print("=== Test iteration #1 === array size: 100 ===")
    print("=== With 100 random integer data items: Create BST, Create BST with sorted input, Create Balanced BST ===")
    print("=== bst1: BST, bst2: BST created with sorted input, balancedTree: Balanced BST ===")
    print("=== Execute Same item search in all these BST and Record number of comparison needed ===")
    
    # === test run # 1 ===    
    randarr = np.random.randint(0, 1000, 100) # Generate random array of 100 integers between (0,1000)    
    searchItem = randarr[np.random.randint(0, len(randarr), 1)[0]] # randomly initialize search item
    bst1 = BST()  # create basic BST data structure
    for item in randarr:
        bst1.insert(item)   # insert all items from the 'int' array in the BST
    # Find 'searchItem' in the BST and if found displays how many comparison done till it found.
    print(f">>> Search in 'bst1' for {searchItem}:", f"Found by {bst1.comparisonCount} comparisons" if bst1.search(searchItem) else "Not found")
        
    # === test run # 2 ===    
    bst2 = BST() # create another BST
    #Input array sorted then inserted in this BST)    
    for item in sorted(randarr):
        bst2.insert(item)        
    print(f">>> Search in 'bst2, created with sorted input' for {searchItem}:", f"Found by {bst2.comparisonCount} comparisons" if bst2.search(searchItem) else "Not found")

    # === test run # 3 === Balanced BST    
    balancedTree = BalancedTree()
    balancedTree.Root = build_balanced_bst(sorted(randarr)) # create Balanced BST with the same input data    
    print(f">>> Search in 'Balanced BST' for {searchItem}:", f"Found by {balancedTree.comparisonCount} comparisons" if balancedTree.search(searchItem) else "Not found")


    print("\n\n=== Test iteration #2 === array size: 500 ===")
    print("=== With 500 integer data items: Create BST, Create BST with sorted input, Create Balanced BST ===")
    print("=== bst1: BST, bst2: BST created with sorted input, balancedTree: Balanced BST ===")
    print("=== Execute Same item search in all these BST and Record number of comparison needed ===")
    
    # === test run # 1 ===
    #print("=== Test 1 ===")    
    #print("=== Execute Same item search in all these BST and Record number of comparison needed ===")
    randarr = np.random.randint(0, 1000, 500) # Generate random array of 500 integers between (0,1000)    
    searchItem = randarr[np.random.randint(0, len(randarr), 1)[0]] # randomly initialize search item
    bst1 = BST()  # create basic BST data structure
    for item in randarr:
        bst1.insert(item)   # insert all items from the 'int' array in the BST
    # Find 'searchItem' in the BST and if found displays how many comparison done till it found.
    print(f">>> Search in 'bst1' for {searchItem}:", f"Found by {bst1.comparisonCount} comparisons" if bst1.search(searchItem) else "Not found")
        
    # === test run # 2 ===    
    bst2 = BST() # create another BST
    #Input array sorted then inserted in this BST)    
    for item in sorted(randarr):
        bst2.insert(item)        
    print(f">>> Search in 'bst2, created with sorted input' for {searchItem}:", f"Found by {bst2.comparisonCount} comparisons" if bst2.search(searchItem) else "Not found")

    # === test run # 3 === Balanced BST
    balancedTree = BalancedTree()
    balancedTree.Root = build_balanced_bst(sorted(randarr)) # create Balanced BST with the same input data    
    print(f">>> Search in 'Balanced BST' for {searchItem}:", f"Found by {balancedTree.comparisonCount} comparisons" if balancedTree.search(searchItem) else "Not found")
    

    print("\n\n=== Test iteration #3 === array size: 1000 ===")
    print("=== With 1000 integer data items: Create BST, Create BST with sorted input, Create Balanced BST ===")
    print("=== bst1: BST, bst2: BST created with sorted input, balancedTree: Balanced BST ===")
    print("=== Execute Same item search in all these BST and Record number of comparison needed ===")

    # === test run # 1 ===    
    randarr = np.random.randint(0, 1000, 1000) # Generate random array of 10000 integers between (0,1000)
    #print("Input: int array, random value range:(0-1000), array size =", len(randarr))    
    searchItem = randarr[np.random.randint(0, len(randarr), 1)[0]] # randomly initialize search item
    bst1 = BST()  # create basic BST data structure
    for item in randarr:
        bst1.insert(item)   # insert all items from the 'int' array in the BST
    # Find 'searchItem' in the BST and if found displays how many comparison done till it found.
    print(f">>> Search in 'bst1' for {searchItem}:", f"Found by {bst1.comparisonCount} comparisons" if bst1.search(searchItem) else "Not found")
        
    # === test run # 2 ===    
    bst2 = BST() # create another BST
    #Input array sorted then inserted in this BST)    
    for item in sorted(randarr):
        bst2.insert(item)        
    print(f">>> Search in 'bst2, created with sorted input' for {searchItem}:", f"Found by {bst2.comparisonCount} comparisons" if bst2.search(searchItem) else "Not found")

    # === test run # 3 === Balanced BST    
    balancedTree = BalancedTree()
    balancedTree.Root = build_balanced_bst(sorted(randarr)) # create Balanced BST with the same input data
    print(f">>> Search in 'Balanced BST' for {searchItem}:", f"Found by {balancedTree.comparisonCount} comparisons" if balancedTree.search(searchItem) else "Not found")
    return
    

if __name__ == "__main__":
    clearScreen()
    print("=== CSC506 - Module 6: Portfolio Milestone ===")
    print("=== Analysis and Optimization ===")
    print("-------------------------------------------\n")
    print("=== Different BST and Search Algorithm ===")
    print("=== Tests executed with different array size having random intergers ===")
    print("=== Data Structure performance: Please notice the Data Structure, input size and Comparison count (or execution time) ===\n")

    executionTimes = run_tests()
    # Results already displayed in run_tests()
    