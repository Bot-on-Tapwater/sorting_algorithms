#!/usr/bin/python3
#bubble sort
#insertion sort

if __name__ == '__main__':

	# Our unsorted list
	unsorted_list = [19, 48, 99, 71, 13, 52, 96, 73, 86, 7]

	while False:		

		# swap helps us know if our list is already sorted in ascending order
		swap = 1
		count = 1
		loop = 1

		while(swap == 1):
			# initiate swap to zero
			swap = 0

			# loop through indices of our unsorted list
			for i in range(len(unsorted_list) - count):			
				try:
					# check if 
					if (unsorted_list[i] > unsorted_list[i + 1]):
						unsorted_list[i], unsorted_list[i + 1] = unsorted_list[i + 1], unsorted_list[i]
						swap = 1
						print(f"\t{unsorted_list}")
				
				except IndexError:
					pass
					
				finally:
					loop += 1		
			count += 1

		print(loop)