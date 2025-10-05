# MS - Artificial Intelligence and Machine Learning
# Course: CSC506 - Design and Analysis of Algorithms
# Professor: Dr. Jonathan Vanover
# Module 4: Portfolio Milestone
# Created by Mukul Mondal
# Saturday, October 4, 2025
#
# Python Program:
#

'''
Problem statement:

Algorithm Implementation and Testing

Implement the chosen algorithms according to your project plan.
Develop necessary input generation mechanisms to test algorithms comprehensively.
Gather empirical data by running algorithms on various inputs.
Document the implementation process and the collected data.

I chose:
Merge Sort Algorithm and Binary Search Algorithm.
'''

from typing import List
import numpy as np
from numpy.core.fromnumeric import sort
from numpy.core.numeric import array_equal
from numpy.random import rand
import math
from time import sleep, time
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


# Binary search Algorithm implementation, runs on sorted array
# It should work on int, double, char array data types
def binary_search(arr, low:int, high:int, searchItem:int) -> int:
    if arr is None or len(arr) < 1 or low < 0 or low > high:
        return -1
    mid = low + (high - low) // 2
    if arr[mid] == searchItem: # found item
        return mid
    else:
        # not found above. So, apply divide and conquer strategy
        return binary_search(arr, low, mid-1, searchItem) if arr[mid] > searchItem \
        else   binary_search(arr, mid+1, high, searchItem)


# Merge Sort Algorithm implementation
# It should work on int, double, char array data types
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        
        # divide into 2 halves
        L = np.copy(arr[:mid])
        R = np.copy(arr[mid:])

        # apply divide and conquer strategy
        merge_sort(L) # Sorting the first half            
        merge_sort(R) # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return


# Main test function
# Executes Algorithms
def run_tests():
    """
    Runs algorithms on different inputs.
    Record execution times; this will help to understand the scalability of the algorithm.
    Merge Sort algorithms' output verified with the output of: np.sort(<same input array>).
    Also item searched after sorting.
    
    Parameters
    ----------
    None

    Return
    ----------
    times -> List of execution times
    """

    times = []

    # === test run # 1 ===
    print("=== Test 1 ===")    
    # Prepare input
    randarr = np.random.randint(0, 1000, 100) # Generate random array of 100 integers between (0,1000)
    print("input array size =", len(randarr))
    searchDataItem = randarr[np.random.randint(0,len(randarr))] # choose one random data item for search test
    sorted_arr = np.sort(np.copy(randarr)) # expected output

    start = time()
    merge_sort(randarr)
    end = time()
    
    # check result with expected output
    # apply binary_search for a dataitem
    if np.array_equal(sorted_arr, randarr) == False:
        print("Merge Sort : Error")
    else:
        print("merge_sort(..) : Success")
        searchItemFoundIndex = binary_search(randarr, 0, len(randarr)-1, searchDataItem)
        if searchItemFoundIndex != -1:            
            print("binary_search(..) : Success")
            print("merge_sort(..) : Execution time =", end-start)
            times.append(end-start)
        else:
            print("Binary Search : Error")

    # === test run # 2 ===
    print("\n=== Test 2 ===")
    # Prepare input
    randarr = np.random.randint(0, 100, 1000) # Generate random array of 1000 integers between (0,100)
    print("input array size =", len(randarr))
    searchDataItem = randarr[np.random.randint(0,len(randarr))] # choose one random data item for search test
    sorted_arr = np.sort(np.copy(randarr)) # expected output

    start = time()
    merge_sort(randarr)
    end = time()
    
    # check result with expected output
    # apply binary_search for a dataitem
    if np.array_equal(sorted_arr, randarr) == False:        
        print("Merge Sort : Error")
    else:
        print("merge_sort(..) : Success")
        searchItemFoundIndex = binary_search(randarr, 0, len(randarr)-1, searchDataItem)
        if searchItemFoundIndex != -1:            
            print("binary_search(..) : Success")
            print("merge_sort(..) : Execution time =", end-start)
            times.append(end-start)
        else:
            print("Binary Search : Error")

    # === test run # 3 ===
    print("\n=== Test 3 ===")
    # Prepare input
    randarr = np.random.randint(-100, 100, 200) # Generate random array of 200 integers between (-100,100)
    print("input array size =", len(randarr))
    searchDataItem = randarr[np.random.randint(0,len(randarr))] # choose one random data item for search test
    sorted_arr = np.sort(np.copy(randarr)) # expected output

    start = time()
    merge_sort(randarr)
    end = time()
    
    # check result with expected output
    # apply binary_search for a dataitem
    if np.array_equal(sorted_arr, randarr) == False:
        print("Merge Sort : Error")
    else:
        print("merge_sort(..) : Success")
        searchItemFoundIndex = binary_search(randarr, 0, len(randarr)-1, searchDataItem)
        if searchItemFoundIndex != -1:            
            print("binary_search(..) : Success")
            print("merge_sort(..) : Execution time =", end-start)
            times.append(end-start)
        else:
            print("Binary Search : Error")

    # === test run # 4 ===
    print("\n=== Test 4 ===")
    # Prepare input, edge case : single element
    randarr = np.random.randint(-100, 100, 1) # Generate random array of 1 integer between (-100,100)
    print("input array size =", len(randarr))
    searchDataItem = randarr[0] # choose existing data item for search test
    sorted_arr = np.sort(np.copy(randarr)) # expected output
    
    start = time()
    merge_sort(randarr)
    end = time()
        
    # check result with expected output
    # apply binary_search for a dataitem
    if np.array_equal(sorted_arr, randarr) == False:        
        print("Merge Sort : Error")
    else:
        print("merge_sort(..) : Success")
        searchItemFoundIndex = binary_search(randarr, 0, len(randarr)-1, searchDataItem)
        searchItemNotFoundIndex = binary_search(randarr, 0, len(randarr)-1, searchDataItem+10)
        if searchItemFoundIndex != -1 and searchItemNotFoundIndex == -1:            
            print("binary_search(..) : Success")
            print("merge_sort(..) : Execution time =", end-start)
            times.append(end-start)
        else:
            print("Binary Search : Error")

    # === test run # 5 ===
    print("\n=== Test 5 ===")
    print("input array size = 0")
    # Prepare input, edge case : no element
    randarr:int = [] # empty array
    sorted_arr:int = [] # expected output

    start = time()
    merge_sort(randarr)
    end = time()
    
    # check result with expected output
    # apply binary_search for a dataitem
    if np.array_equal(sorted_arr, randarr) == False:       
        print("Merge Sort : Error")
    else:
        print("merge_sort(..) : Success")
        searchItemFoundIndex = binary_search(randarr, 0, 0, 10)
        if searchItemFoundIndex == -1:            
            print("binary_search(..) : Success")
            print("merge_sort(..) : Execution time =", end-start)
            times.append(end-start)
        else:
            print("Binary Search : Error")

    return times  # return execution times



# Main execution entry point
# It runs tests multiple times with different input array.
# It also displays the execution times for the algorithm.
# typical execution result:
""" 
=== Test 1 ===
input array size = 100
merge_sort(..) : Success
binary_search(..) : Success
merge_sort(..) : Execution time = 0.0005068778991699219

=== Test 2 ===
input array size = 1000
merge_sort(..) : Success
binary_search(..) : Success
merge_sort(..) : Execution time = 0.008499860763549805

=== Test 3 ===
input array size = 200
merge_sort(..) : Success
binary_search(..) : Success
merge_sort(..) : Execution time = 0.0016815662384033203

=== Test 4 ===
input array size = 1
merge_sort(..) : Success
binary_search(..) : Success
merge_sort(..) : Execution time = 9.5367431640625e-07

=== Test 5 ===
input array size = 0
merge_sort(..) : Success
binary_search(..) : Success
merge_sort(..) : Execution time = 9.5367431640625e-07 
"""

if __name__ == "__main__":
    clearScreen()
    print("=== CSC506 - Module 4: Portfolio Milestone ===")
    print("=== Algorithm implementaion and tests ===")
    print("-------------------------------------------\n")
    print("=== Merge Sort and Binary Search Algorithms ===")
    print("=== Tests executed with different array size having random intergers ===")
    print("=== Scalability: Please observe the input size and execution time ===\n")

    executionTimes = run_tests()
    #execution times already displayed in run_tests() 
    