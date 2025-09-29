# MS - Artificial Intelligence and Machine Learning
# Course: CSC506 - Design and Analysis of Algorithms
# Professor: Dr. Jonathan Vanover
# Module 3: Critical Thinking
# Created by Mukul Mondal
# Sunday, September 28, 2025
#
# Python Program:
#

'''
Problem statement:

Dive into the task of enhancing the efficiency of a hospital's patient records system by comparing the 
Bubble Sort and Merge Sort algorithms.

Algorithm: Bubble Sort and Merge Sort
Analysis (one page, excluding cover and references): Analyze the time complexity of both sorting 
algorithms, elucidate the conditions under which each performs optimally in the medical records 
context, and discuss the critical problem of sorting in healthcare. Justify the chosen data structures 
and consider external factors affecting efficiency and the lower bound.
Please ensure that your submission includes the following components:

Source code file(s) containing the program implementation.
A 1-page paper (excluding the cover and references) explaining the program's purpose, the obstacles 
faced during its development, and the skills acquired. The paper should also include screenshots 
showcasing the successful execution of the program.
'''

from typing import List
import numpy as np
from numpy.core.fromnumeric import sort
from numpy.core.numeric import array_equal
from numpy.random import rand
import math
from datetime import datetime, date, timedelta 
from time import sleep, time
from enum import Enum
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


# Enum representing Patient's Gender
class Gender(Enum):
    MALE = 1
    FEMALE = 2

# Class representing Patient for the Hospital
class Patient:
    def __init__(self, id:int, name:str, dob:date, gender:Gender):
        self.ID: int = id                       # Patient ID
        self.Name: str = name.lstrip().rstrip() # Patient Name
        self.DOB: date = dob                    # Patient DOB
        self.Gender: Gender = gender            # Patient Gender

# Class representing Patient's Visit to the hospital
class Visit:
    def __init__(self, id:int, patientID:int, visitDate:date, insurance:str):
        self.ID: int = id                       # Visit ID
        self.PatientID = patientID              # Patient ID
        self.VisitDate: date = visitDate        # Patient Visit Date
        self.Insurance: str = insurance.lstrip().rstrip() # Patient Insurance

# Class representing Patient's Medication by the hospital
class Medication:
    def __init__(self, rxid:int, patientID:int, drugname:str, dosage: int):
        self.ID: int = rxid                     # Medication ID
        self.PatientID = patientID              # Patient ID
        self.DrugName: str = drugname.lstrip().rstrip() # Drug Name
        self.Dosage: int = dosage               # Medication dosage

# Collection representing insurance provider
InsuranceProviders = ["bluecross", "cigna", "aetna", "unitedhealth"] # few insurance providers

# This class has the main implementation of the requirements.
# It has implementation of sorting algorithms
#    Bubble Sort : def bubble_sort(self, arr, sortColumn):
#    Merge Sort : def merge_sort(self, arr, sortColumn):
# Sorting options implemented for some important properties
# I can sorting options for more/all properties of these model classes
#
# I've added inline comments in multiple places, for user reference.
#
class Sort:
    # Sorting Algorithm Implementations
    # Bubble Sort Algorithm
    def bubble_sort(self, arr, sortColumn:str):
        if len(arr) < 2:
            return arr
        
        temp: any
        i: int
        repeat: bool = True
        while repeat:
            repeat = False
            for i in range(len(arr)-1):
                if type(arr[i]) == Patient and sortColumn == 'Name':
                    if arr[i].Name > arr[i+1].Name:
                        temp = arr[i]
                        arr[i] = arr[i+1]
                        arr[i+1] = temp
                        repeat = True
                elif type(arr[i]) == Visit and sortColumn == 'VisitDate':
                    if arr[i].VisitDate > arr[i+1].VisitDate:
                        temp = arr[i]
                        arr[i] = arr[i+1]
                        arr[i+1] = temp
                        repeat = True
                elif type(arr[i]) == Medication and sortColumn == 'PatientID':
                    if arr[i].PatientID > arr[i+1].PatientID:
                        temp = arr[i]
                        arr[i] = arr[i+1]
                        arr[i+1] = temp
                        repeat = True
        return
        

    # Merge Sort Algorithm
    def merge_sort(self, arr, sortColumn:str):
        if len(arr) > 1:    
            mid = len(arr)//2
            
            # divide into 2 halves
            L = np.copy(arr[:mid])
            R = np.copy(arr[mid:])

            self.merge_sort(L,sortColumn) # Sorting the first half            
            self.merge_sort(R,sortColumn) # Sorting the second half

            i = j = k = 0

            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if type(arr[i]) == Patient and sortColumn == 'Name':
                    if L[i].Name < R[j].Name:
                        arr[k] = L[i]
                        i += 1
                    else:
                        arr[k] = R[j]
                        j += 1
                elif type(arr[i]) == Visit and sortColumn == 'VisitDate':
                    if L[i].VisitDate < R[j].VisitDate:
                        arr[k] = L[i]
                        i += 1
                    else:
                        arr[k] = R[j]
                        j += 1
                elif type(arr[i]) == Medication and sortColumn == 'PatientID':
                    if L[i].PatientID < R[j].PatientID:
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
    

# Main execution entry point
# It creates object of the above class and calls all required functions.
#
# It displays the execution times for each algorithm.
# typical execution result:
# Patients: container of Patient objects.
# Patients has  100  objects.
# Running Sorting algorithms on property: Name
# Bubble Sort. Execution time :  0.0011434555053710938
# Merge Sort. Execution time :  0.000823974609375
# 

if __name__ == "__main__":
    clearScreen()
    print("=== CSC506 - Module 3: Critical Thinking ===")
    print("=== Sorting Algorithm Comparator ===")
    print("-------------------------------------------\n")

    # Create Random test data
    # 100 Patient, 1000 Visit, 5000 Medication
    allChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # used for Patient.Name <== composed of randomly selected 3 characters
    patientIDs = list(range(1, 101))
    start_date = datetime(1970, 1, 1)
    end_date = datetime(2025, 8, 31)
    delta = end_date - start_date
    Patients = []
    Visits = []
    Medications = []
    for pid in patientIDs:
        Patients.append(Patient(pid, allChars[np.random.randint(0,25)] + allChars[np.random.randint(0,25)] + allChars[np.random.randint(0,25)], start_date + timedelta(days=np.random.randint(0, delta.days)), np.random.choice(list(Gender))))
    
    visitIDs = list(range(1, 1001))
    for vid in visitIDs:
        pid = np.random.randint(0,len(patientIDs))
        delta = end_date - Patients[pid].DOB
        Visits.append(Visit(vid, pid, Patients[pid].DOB + timedelta(days=np.random.randint(0, delta.days)), np.random.choice(InsuranceProviders)))

    medicationIDs = list(range(1, 5001))
    for id in medicationIDs:
        pid = np.random.randint(0,len(patientIDs))        
        Medications.append(Medication(id, pid, "Drug-" + str(np.random.randint(0, 100)), np.random.randint(1, 5)))

    
    sorter = Sort()
    resultsBubble = []
    resultsMerge = []    
    inputArraySize: int    

    print("Patients: container of Patient objects.")
    print("Patients has ", len(Patients), " objects.")
    print("Running Sorting algorithms on property: Name(str)")
    start = time()
    sorter.bubble_sort(Patients,'Name')
    end = time()
    print("Bubble Sort. Execution time : ", end-start)
    
    start = time()
    sorter.merge_sort(Patients,'Name')
    end = time()
    print("Merge Sort. Execution time : ", end-start)

    print("")

    print("Visits: container of Visit objects.")
    print("Visits has ", len(Visits), " objects.")
    print("Running Sorting algorithms on property: VisitDate(Date)")
    start = time()
    sorter.bubble_sort(Visits,'VisitDate')
    end = time()
    print("Bubble Sort. Execution time : ", end-start)
    
    start = time()
    sorter.merge_sort(Visits,'VisitDate')
    end = time()
    print("Merge Sort. Execution time : ", end-start)

    print("")

    print("Medications: container of Medication objects.")
    print("Medications has ", len(Medications), " objects.")
    print("Running Sorting algorithms on property: PatientID(int)")
    start = time()
    sorter.bubble_sort(Medications,'PatientID')
    end = time()
    print("Bubble Sort. Medications - PatientID : ", end-start)
    
    start = time()
    sorter.merge_sort(Medications,'PatientID')
    end = time()
    print("Merge Sort. Medications - PatientID : ", end-start)

