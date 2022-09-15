#quick sort complexity: kind of complicated
#worst case: same as bubble sort O(n^2)
#average: O(nlog(n))
#best case: O(nlog(n))
#-> not good for almost sorted arrays -> worst case every time
#space complexity: O(log(n)) constant

def partition(array, first_index, last_index):
    #choose last element as pivot
    pivot = array[last_index]
    #pointer for gretaer element, trying to figure out -1
    i = first_index - 1

    for j in range(first_index, last_index):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]

    #swap pivot with greater element
    array[i+1] , array[last_index] = array[last_index], array[i+1]

    return i+1 #return partition position

def quickSort(array, first_index, last_index):
    if first_index < last_index:
        pi = partition (array, first_index, last_index)

        #recursive on left side
        quickSort(array, first_index, pi - 1)
        #recursive on right side
        quickSort(array, pi + 1, last_index)






    

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
quickSort(test, 0, len(test) - 1 )
print (test)
    