import random
import sorting
import time

# t1 = time.time()
# time.sleep(3)
# t2 = time.time()
# print(t2 - t1) ==> +- 3sec

my_list1 = [random.randint(0, 1000)
            for i in range(10000)]

my_list2 = [element for element in my_list1]

t1 = time.time()
sorting.sort_selection(my_list1)
t2 = time.time()

t3 = time.time()
my_list2.sort()
t4 = time.time()

print("tri_selection :", t2 - t1)
print("tri_sort :", t4 - t3)