# Bubble Sort: Naive Approach: Looping through the Array while comparing Elements, Looping until no switch is done through a loop
#long run time, because sorting takes a lot of loops  -> not good for large data pools
#time complexity: O(n^2), Space complexity: O(1)

sort_list = [1, 12, 33, 2, 8, 0, 9, 34, 66, 69]

def bubble(list1):
    change_made = True
    while change_made:
        change_made = False
        for x in range(len(list1)-1):
            if list1[x] > list1[x+1]:
                list1[x], list1[x+1] = list1[x+1], list1[x]
                change_made = True


bubble(sort_list)
print(sort_list)



        