#Marissa Tracy
#Problem 1
import random
from sys import stdout
import sys
import fileinput
import numpy

with open(sys.argv[1]) as file: #Stores in array
    array = open(sys.argv[1]).read().split() #reading file
    length = len(array) #gets length of array in file
    print array #check

def reversePairs(array):
    return merge_reversePairs(array)[1] #returns result

def merge_reversePairs(array):
    if len(array) <= 1: #if the array is 1 or less elements there cannot be any reverses
        return array, 0
    middle = int( len(array) / 2 ) #calculates middle of array
    subarray1, a = merge_reversePairs(array[:middle]) #assign each subarray
    subarray2, b = merge_reversePairs(array[middle:]) #assign each subarray
    result, c = mergeSort(subarray1, subarray2) #to find reverses, you need to sort the subarays
    return result, (a + b + c)

def mergeSort(subarray1, subarray2):
    result = []
    count = 0 #initialize count
    i, j = 0, 0 #initialize loop variables
    subarray1_len = len(subarray1) #find length of subarray
    subarray2_len = len(subarray2) #find length of subarray
    while i < subarray1_len and j < subarray2_len: #loop through
        if subarray1[i] <= subarray2[j]: #if there is a reverse pair
            result.append(subarray1[i]) #count
            i += 1
        else:
            result.append(subarray2[j]) #no reverse array, continue search
            count += subarray1_len - i
            j += 1
    result += subarray1[i:]
    result += subarray2[j:]
    return result, count

print reversePairs(array)
