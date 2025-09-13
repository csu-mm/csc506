# MS - Artificial Intelligence and Machine Learning
# Course: CSC506 - Design and Analysis of Algorithms
# Professor: Dr. Jonathan Vanover
# Module 1: Critical Thinking
# Created by Mukul Mondal
# Saturday, September 13, 2025
#
# Python Program:
#

'''
Problem statement:

Address the task of efficiently searching for a specific item in a large online marketplace
database using a linear search algorithm. 

Algorithm: Linear Search 
Analysis (one page, excluding cover and references): Delve into why linear search is 
         applicable for this scenario, examine its time complexity in the context of 
         online searches, and discuss how the chosen data structure affects its 
         performance. Identify external factors that could influence the lower 
         bound of this solution.

Please ensure that your submission includes the following components:
Completed Linear Search Algorithm
A 1-page paper (excluding the cover and references) explaining the program's purpose, 
the obstacles faced during its development, and the skills acquired. The paper should 
also include screenshots showcasing the successful execution of the program.
'''
from os import system, name
import numpy as np

#
# Program description.
# 
# This is just a helper function to clear the screen
# This is not required, per problem statement.
def clearScreen():
    if name == 'nt':  # For windows system
        _ = system('cls')    
    else:             # for non-windows system
        _ = system('clear')
    print("")
    return


# assumptions: 
# 1. Products are identified or searched by it's name.
# 2. Product names, in lowercase, are stored in an array.
# 3. Product names are case-insensitive for our business logic.
products_online_marketplace = np.array(['product1', 'product2','product3','iphone16', 'ram32gb','toy1', 'router1', 'baseball1'])


# search method
# method details:
# input: string: product name
# output: int: existing product, it's index in the array
#            : non-existing product, -1
#            : invalid input, -1
def SearchProduct(prodName: str) -> int:
    foundIndex: int = -1
    if not prodName:
        return foundIndex
    else:
        prodName = prodName.lstrip().rstrip().lower()

    for i in range(len(products_online_marketplace)):
        if products_online_marketplace[i].lower() == prodName:
            foundIndex = i
    return foundIndex

# search method caller
def execute_module1_ct():
    searchProd: str = input('Enter the Product name, you want to search:\n')
    if not searchProd:
        print("Please try again with valid Product name.")
    else:
        indx = SearchProduct(searchProd)
        if indx == -1:
            print("Product not found. Please try again...")
        else:
            print(f"Found. Product: {products_online_marketplace[indx]}, at Index {indx}")
    return

if __name__ == "__main__":
    clearScreen()
    print("=== Module 1: Critical Thinking ===\n")    
    execute_module1_ct()