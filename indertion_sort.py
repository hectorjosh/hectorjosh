#INSERTION SORT ALGORITHM

#this inserts elements in sorted positions
def insertion_sort(array):
	#checking each element 
	for i in range(1,len(array)):
		#insert is the element to be inserted in the sorted position
		insert = array[i]
		#we are moving from right to left so this j position explains why we subtract 
		j = i - 1
		#the last condition fulfills the left most position because a list index can't be less than zero
		while insert < array[j] and j >= 0:
			#if yes, the current element at j position goes to the right
			array[j+1] = array[j]
			#we reduce the j index by 1 to go further to the left
			j = j - 1
		#if the whole loop is over,we then insert the element	
		array[j+1] = insert
		
	return array
	
nums = [2-3,45,56,24,78,65,12,67,4.5,7,75,26]
sorted_nums = insertion_sort(nums)
print(sorted_nums)