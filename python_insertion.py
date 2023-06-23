#!/usr/bin/python3

if __name__ == "__main__":
    
	unsorted_list = [19, 48, 99, 71, 13, 52, 96, 73, 86, 7]

	# loop = 1

	# Loop through the list

	# Comparing to adjacent elems i.e [left element "le"] & [right element "re"]

	# If le is smaller than the re no swap occurs, compare the next set of pairs

	# If le is larger than the re swap the two values

	# After swap compare [New left element "nle"] with the element to it's left

	# if nle is the smaller of the two do the swap again and do this until the element to the left of nle is smaller than nle or if nle arrives at index [0] (start of list)


	for i in range(1, len(unsorted_list)):
		# helps us remember our index position
		key = unsorted_list[i]

		# index to the predecessor element of our current element
		j = i - 1

		# Check pairs upto pair at index 0 and 1 no negative indices, also check if pred is larger than current element
		while j >= 0 and  key < unsorted_list[j]:
			# (j + 1) == index i, thus swap i and j values
			unsorted_list[j + 1] = unsorted_list[j]
			# Keep backtracking in our list until while condition evaluates to false
			j -= 1

		# print(f"\tBefore last code {unsorted_list}")	
		unsorted_list[j + 1] = key
		print(unsorted_list)