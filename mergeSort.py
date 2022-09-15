#Divide and Conquer Principal:
#-break up array into segments of 1 element each
#-built up into arrays of size 2 and 1 (depending if even or uneven number of data elements)
#-sort insides of smaller arrays into new sorted array of same size
#combine 2 sorted arrays each into new arrays and sort the new elements
#continue until you have 1 sorted array
#combine the first element of each array to see which goes first into the big array, and move the element from the chosen array one further
#efficiency: time: O(n log(n)), space: O(n)

def mergeSort(array):
    if len(array) > 1:
        #middle of the array
        mid = len(array)//2

        #seperate in left and right side of the array
        left = array[:mid]
        right = array[mid:]

        #sorting left and right side
        mergeSort(left)
        mergeSort(right)

        i = j = k = 0
        #sort the array, 
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

def printList(array):
    for i in range(len(array)):
        print(array[i], end = " ")
    print("\n")



if __name__ == "__main__":
    array = [12, 11, 13, 5, 6, 7]
    print("Given array is:", end = "\n")
    printList(array)
    mergeSort(array)
    print("Sorted array is:", end = "\n")
    printList(array)

        
