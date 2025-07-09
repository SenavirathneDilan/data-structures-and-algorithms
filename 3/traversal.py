from array import *


arr1 = array('i', range(6))
arr2 = array('d', [1.3, 1.63, 1.8])

arr1.insert(2,9)
# print(arr1)




def access_element(array, index):
    if index > len(array):
        print('there are not any element in this index')
    else:
        print(array[index])
        
# access_element(arr1, 4 )


def find_value(array, value):
    for i, v in enumerate(array):
        if v != value:
            continue
        else:
            print('value Found. index {}'.format(i))
            return i 
            
            
find_value(arr1, 5)

def find_index(arr, value):
    for i,v in arr:
        if v == value:
            return i
    else:
        print('cannot find the value in the given list')
        return -1
    
    
def delete_element(arr, value):
    index = find_index(arr, value)
    if index != -1:
        