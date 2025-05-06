def pairs(k, arr):
    # Write your code here
    counter = 0
    hashTable = {}
    
    for i in arr:
        hashTable[i] = True
    
    for i in range(len(arr)):
        if arr[i] + k in hashTable:
            counter += 1
                
    return counter
