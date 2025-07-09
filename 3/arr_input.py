import array

my_arr = array.array('i', range(5,40,3))

print(my_arr)

my_arr.insert(len(my_arr), 999)

print(my_arr)
