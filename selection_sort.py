#SELECTION SORT ALGORITHM 
import sys
#this checks for the minimum element and swaps it with the current element at a particular position
def selection_sort(array):
                                	for i in range(len(array)):
                                		#this is our current lowest index
                                		min_index = i
                                		#we start looping from i+1 index coz we are checking from the right
                                		for j in range(i+1, len(array)):
                                			if array[min_index] > array[j]:
                                				#this means the j index represents the smallest element among the two being compared
                                				min_index = j
                                				
                                		#we then swap the elements from the outer loop but not inside the nested loop
                                		temp = array[i]
                                		array[i] = array[min_index]
                                		array[min_index] = temp
                                	return array
nums = [23,45,56,24,78,65,12,67]	
selection_sort(nums)
if __name__ == "__main__":
	print("Direct function run")
	print(selection_sort(nums))
else:
	print("Indirect function run")
	
#print(*objects,sep=" ",end="/n",file = sys.stdout, flush=False)
			