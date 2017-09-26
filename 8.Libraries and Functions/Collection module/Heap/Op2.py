# Python code to demonstrate working of
# heappushpop() and heapreplce()

# importing "heapq" to implement heap queue
import heapq

# initializing list 1
li1 = [5, 7, 9, 4, 3]

# initializing list 2
li2 = [5, 7, 9, 4, 3]

# using heapify() to convert list into heap
heapq.heapify(li1)
heapq.heapify(li2)

# printing created heap
print("The  heap1 is : ", end="")
print(list(li1))
# printing created heap
print("The  heap2 is : ", end="")
print(list(li2))

# using heappushpop() to push and pop items simultaneously
# pops 2
print("1The popped item using heappushpop() is : ", end="")
print(heapq.heappushpop(li1, 2))

# using heapreplace() to push and pop items simultaneously
# pops 3
print("2he popped item using heapreplace() is : ", end="")
print(heapq.heapreplace(li2, 2))

# printing created heap
print("The modified heap1 is : ", end="")
print(list(li1))
print("The modified heap2 is : ", end="")
print(list(li2))


'''

4. heappushpop(heap, ele) :- This function combines the functioning of both push and 
pop operations in one statement, increasing efficiency. Heap order is maintained after this operation.

5. heapreplace(heap, ele) :- This function also inserts and pops element in one statement,
 but it is different from above function. In this, element is first popped, then element is pushed.
 i.e, the value larger than the pushed value can be returned.

'''
