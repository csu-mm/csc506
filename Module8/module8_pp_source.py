# MS - Artificial Intelligence and Machine Learning
# Course: CSC506 - Design and Analysis of Algorithms
# Professor: Dr. Jonathan Vanover
# Module 8: Portfolio Project
# Created by Mukul Mondal
# Sunday, November 2, 2025
#
# Python Program:
#

'''
Problem statement:

Final Presentation and Submission

Create a presentation with at least 8 slides or a two page write up highlighting the project's goals, methodology, analysis, and outcomes.
Include visuals, graphs, and code snippets to support your presentation.
Review and refine your project documentation, ensuring clarity and completeness.
Submit the project plan along with the algorithm choices for approval.

Please ensure that your submission includes the following components:
Source code file(s), documentation, and any supplementary materials.
A 2-page paper (excluding the cover and references) or 8-slide presentation explaining the program's purpose, 
the obstacles faced during its development, and the skills acquired. The paper should also include screenshots 
showcasing the successful execution of the program.

My project: Sorting Algorithm Comparator.
Develop a program to compare sorting algorithms (e.g., Bubble, Merge, Quick, Counting Sort) using various inputs.
Implement algorithms, gather data, and analyze/compare execution time(complexity).
'''

from os import system, name
import numpy as np
from time import time



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
#    Counting Sort : def Counting_sort(self, inputArray):
# run_all(..) is the main function that calls all sorting functions on the same input array,
#    when done executing, it returns an array with execution times for each algorithm type.
#
# I've added inline comments in multiple places, for reference.
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
            * Counting Sort
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
        
        # Counting Sort
        if print_msg:
            print("\nRunning Counting Sort Algorithm...")
        arr_copy_counting = np.copy(arr)
        start = time()
        result_counting_sort = self.Counting_sort(arr_copy_counting)
        end = time()
        times.append(end-start)
        if np.array_equal(sorted_arr, result_counting_sort) == False:
            times.remove(end-start)
            print("Counting Sort : Error")
        
        return times  # executed all four sorting algorithms


    # Sorting Algorithm Implementations
    # 
    # Counting sort Algorithm implementation function
    def Counting_sort(self, arr):
        if len(arr) < 2:
            return arr
        
        # find minimum and maximum items in the input array.
        itemMinValue: int = arr[0]
        itemMaxValue: int = arr[0]
        i: int = 0
        while i < len(arr):
            if itemMinValue > arr[i]:
                itemMinValue = arr[i]
            if itemMaxValue < arr[i]:
                itemMaxValue = arr[i]
            i += 1

        # Create new 'int' array to capture the occurrence count of each array element in the range(itemMinValue - itemMaxValue)
        # initialize all elements of this array with 0
        inputItemOccurrenceCountArray = np.zeros(1+itemMaxValue-itemMinValue, dtype=int)

        # Update the occurrence capture array with element's repeat count
        i = 0
        while i < len(arr):
            inputItemOccurrenceCountArray[arr[i] - itemMinValue] += 1
            i += 1

        # do prefix accumulative sum for each array element
        i = 1
        while i < len(inputItemOccurrenceCountArray):            
            inputItemOccurrenceCountArray[i] += inputItemOccurrenceCountArray[i-1]
            i += 1

        # Create new output 'int' array, same size as input array and initialize each element to 0
        outputArray = np.zeros(len(arr), dtype=int)

        # Fill up the output array, from last to first with max-to-min elements from 'inputArray'.
        # From last to first, only needed to keep the sorting algorithm Stable
        i = len(arr) - 1
        while i >= 0:
            inputItemOccurrenceCountArray[arr[i]-itemMinValue] -= 1
            outputArray[inputItemOccurrenceCountArray[arr[i]-itemMinValue]] = arr[i]
            i -= 1
        return outputArray


    # Bubble Sort Algorithm implementation function
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
        

    # Merge Sort Algorithm implementation function
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
    

    # Quick Sort Algorithm implementation function
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
# typical execution summary result:
# ----- Running Test 10 - Iteration 10 -----
# Input: integer array, size: 700
# Bubble sort == Executed: 100 times. Mean execution time: 0.24628968238830568
# Merge sort == Executed: 100 times. Mean execution time: 0.007438302040100098
# Quick sort == Executed: 100 times. Mean execution time: 0.004209196567535401
# Counting sort == Executed: 100 times. Mean execution time: 0.0026565337181091307
if __name__ == "__main__":
    clearScreen()
    print("=== CSC506 - Module 8: Portfolio Project ===")
    print("=== Sorting Algorithm (Bubble, Merge, Quick, Counting) Comparison ===")
    print("-------------------------------------------\n")

    sorter = Sort()
    resultsBubble = []
    resultsMerge = []
    resultsQuick = []
    resultsCounting = []
    inputArraySize: int

    # Loop through all Iterations
    for test_number in range(10):
        randarr = np.random.randint(100, 999, 2000) # Generate random array of 700 integers in the range: 100-999 
        inputArraySize = len(randarr)
        print("Current iteration input array size:", inputArraySize)
        print("Current iteration input array:")
        print(randarr)
        for count in range (10):
            print("\n----- Running Test {} - Iteration {} -----".format(test_number+1, count+1))
            # Tests functions and append runtime data
            times = sorter.run_all(randarr, print_msg=False)
            if len(times) == 4:
                resultsBubble.append(times[0])
                resultsMerge.append(times[1])
                resultsQuick.append(times[2])
                resultsCounting.append(times[3])

    print("Input: integer array, size:", inputArraySize)
    print("Bubble sort == Executed:", len(resultsBubble), "times. Mean execution time:", np.mean(resultsBubble))
    print("Merge sort == Executed:", len(resultsMerge), "times. Mean execution time:", np.mean(resultsMerge))
    print("Quick sort == Executed:", len(resultsQuick), "times. Mean execution time:", np.mean(resultsQuick))
    print("Counting sort == Executed:", len(resultsCounting), "times. Mean execution time:", np.mean(resultsCounting))
