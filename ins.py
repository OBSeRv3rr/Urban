from namespace.sort import *


data_1 = list(map(int, input().split()))
data_2 = list(map(int, input().split()))
data_3 = list(map(int, input().split()))


bubble_sort(data_1)
selection_sort(data_2)
insertion_sort(data_3)

print(data_1)
print(data_2)
print(data_3)
