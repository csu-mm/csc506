# MS - Artificial Intelligence and Machine Learning
# Course: CSC506 - Design and Analysis of Algorithms
# Professor: Dr. Jonathan Vanover
# Module 2: Portfolio Milestone
# Created by Mukul Mondal
# Sunday, September 21, 2025
#
# Python Program:
#

'''
Problem statement:

Project Planning and Algorithm Selection

Choose a project idea from the list below and finalize your decision.
Prepare a detailed project plan outlining tasks, responsibilities, and timelines.
Research and choose the algorithms you'll implement and analyze for the project.
Submit the project plan along with the algorithm choices for approval.

I chose:
Sorting Algorithm Comparator: Develop a program to compare sorting algorithms 
(e.g., Bubble, Merge, Quick Sort) using various inputs. Implement algorithms, 
gather data, and analyze time complexity.
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


# This class has the main implementation of the requirements.
# It has implementation of sorting algorithms
#    Bubble Sort : def bubble_sort(self, arr):
#    Merge Sort : def merge_sort(self, arr):
#    Quick Sort : def quick_sort(self, array, left, right):
# run_all(..) is the main function that calls all sorting functions on the same input array,
#    when done executing, it returns an array with execution times for each algorithm type.
#
# I've added inline comments in multiple places, for user reference.
#
class Sort:
    
    # Executes Sorting Algorithms
    def run_all(self, arr, print_msg=True):
        """
        Runs all of the sorting functions on the given array.

        Same copy of the input array will be passed to each sorting function.
        Sort algorithms' output verified with the output of: np.sort(<same input array>).

        Parameters
        ----------
        arr : [] The array that will be sorted by each sorting function

        Return
        ----------
        times -> List of execution times for the algorithms in the following order            
            * Bubble Sort
            * Merge Sort
            * Quick Sort
        """

        times = []

        # Create the sorted array
        if print_msg:
            print("\nGenerating a sorted array for comparisons with Numpy's included sort function")
        sorted_arr = np.sort(np.copy(arr))
        
        
        # Bubble Sort
        if print_msg:
            print("\nRunning Bubble Sort Algorithm...")
        arr_copy_bubble = np.copy(arr)
        start = time()
        self.bubble_sort(arr_copy_bubble)
        end = time()
        times.append(end-start)
        if np.array_equal(sorted_arr, arr_copy_bubble) == False:
            times.remove(end-start)
            print("Bubble Sort : Error")


        # Merge Sort
        if print_msg:
            print("\nRunning Merge Sort Algorithm...")
        arr_copy_merge = np.copy(arr)
        start = time()        
        self.merge_sort(arr_copy_merge)
        end = time()
        times.append(end-start)
        if np.array_equal(sorted_arr, arr_copy_merge) == False:
            times.remove(end-start)
            print("Merge Sort : Error")            


        # Quick Sort
        if print_msg:
            print("\nRunning Quick Sort Algorithm...")
        arr_copy_quick = np.copy(arr)
        start = time()
        self.quick_sort(arr_copy_quick, 0, len(arr_copy_quick)-1)
        end = time()
        times.append(end-start)
        if np.array_equal(sorted_arr, arr_copy_quick) == False:
            times.remove(end-start)
            print("Quick Sort : Error")
        
        return times  # executed all three algorithms

    #Sorting Algorithm Implementations
    # Bubble Sort Algorithm
    def bubble_sort(self, arr):
        if len(arr) < 2:
            return arr
        
        temp: int
        i: int
        repeat: bool = True
        while repeat:
            repeat = False
            for i in range(len(arr)-1):
                if arr[i] > arr[i+1]:
                    temp = arr[i]
                    arr[i] = arr[i+1]
                    arr[i+1] = temp
                    repeat = True
        return
        

    # Merge Sort Algorithm
    def merge_sort(self, arr):        
        if len(arr) > 1:    
            mid = len(arr)//2
            
            # divide into 2 halves
            L = np.copy(arr[:mid])
            R = np.copy(arr[mid:])

            self.merge_sort(L) # Sorting the first half            
            self.merge_sort(R) # Sorting the second half

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
    

    # Quick Sort  Algorithm
    def quick_sort(self, array, left, right):
        
        if left < 0 or right - left <= 0:  # Recursive edge/base case
            return

        # Find the next pivot point
        partition_index = self._quicksort_partition(array, left, right)

        # Recursively sort left half of pivot
        self.quick_sort(array, left, partition_index - 1)

        # Recursively sort right half of pivot
        self.quick_sort(array, partition_index + 1, right)
        return

    def _quicksort_partition(self, array, left, right) -> int:
        pivot = array[right]
        i = j = left

        for i in range(left, right):
            if array[i] < pivot:
                array[i], array[j] = array[j], array[i]
                j+= 1

        array[j], array[right] = array[right], array[j]
        return j


# Main execution entry point
# It creates object of the above class and calls all required functions.
# It runs tests multiple times in different iterations.
# It also displays the mean execution times for each algorithm.
# typical execution result:
# ----- Running Test 10 - Iteration 10 -----
# Input: integer array, size:  5000
# Bubble sort == Executed:  100 times. Mean execution time:  9.797896876335145
# Merge sort == Executed:  100 times. Mean execution time:  0.05077141523361206
# Quick sort == Executed:  100 times. Mean execution time:  0.031351776123046876
if __name__ == "__main__":
    clearScreen()
    print("=== CSC506 - Module 2: Portfolio Milestone ===")
    print("=== Sorting Algorithm Comparator ===")
    print("-------------------------------------------\n")

    sorter = Sort()
    resultsBubble = []
    resultsMerge = []
    resultsQuick = []
    inputArraySize: int    

    # Loop through all Iterations
    for test_number in range(10):
        randarr = np.random.randint(0, 10000, 100) # Generate random array of 5000 integers
        inputArraySize = len(randarr)
        print(randarr)
        for count in range (10):
            print("\n----- Running Test {} - Iteration {} -----".format(test_number+1, count+1))
            # Tests functions and append runtime data
            times = sorter.run_all(randarr, print_msg=False)
            if len(times) == 3:
                resultsBubble.append(times[0])
                resultsMerge.append(times[1])
                resultsQuick.append(times[2])

    print("Input: integer array, size: ", inputArraySize)
    print("Bubble sort == Executed: ", len(resultsBubble), "times. Mean execution time: ", np.mean(resultsBubble))
    print("Merge sort == Executed: ", len(resultsMerge), "times. Mean execution time: ", np.mean(resultsMerge))
    print("Quick sort == Executed: ", len(resultsQuick), "times. Mean execution time: ", np.mean(resultsQuick))    
