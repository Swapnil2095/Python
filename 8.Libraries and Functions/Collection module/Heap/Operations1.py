'''
Heap data structure is mainly used to represent a priority queue. 
In Python, it is available using “heapq” module. The property of this data structure 
in python is that each time the smallest of heap element is popped(min heap). 
Whenever elements are pushed or popped, heap structure in maintained. 
The heap[0] element also returns the smallest element each time.

'''

# Python code to demonstrate working of
# heapify(), heappush() and heappop()

# importing "heapq" to implement heap queue
import heapq

# initializing list
li = [5, 7, 9, 1, 3]

# using heapify to convert list into heap
heapq.heapify(li)

# printing created heap
print("The created heap is : ", end="")
print(list(li))

# using heappush() to push elements into heap
# pushes 4
heapq.heappush(li, 4)

# printing modified heap
print("The modified heap after push is : ", end="")
print(list(li))

# using heappop() to pop smallest element
print("The popped and smallest element is : ", end="")
print(heapq.heappop(li))


# printing created heap
print("The modified heap is : ", end="")
print(list(li))