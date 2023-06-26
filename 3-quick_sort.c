#include "sort.h"

/**
 * swap - Swaps two elements in the array if they are different
 * @array: Array of integers
 * @i: Index of the first element
 * @j: Index of the second element
 * @size: The size of the array of integers
 */
void swap(int *array, int i, int j, size_t size)
{
	if (array[i] != array[j])
	{
		int temp = array[i];

		array[i] = array[j];
		array[j] = temp;
		print_array(array, size);
	}
}

/**
 * partition - Lomuto partition function for the quicksort algorithm
 * @array: Array of integers
 * @low: Starting index of the partition
 * @high: Ending index of the partition
 * @size: The size of the array of integers
 * Return: The index of the pivot after partitioning
 */
int partition(int *array, int low, int high, size_t size)
{
	int pivot = array[high]; /* // Pivot is the last element */
	int i = low;
	int j;

	for (j = low; j < high; j++)
	{
		if (array[j] < pivot)
		{
		swap(array, i, j, size);
		i++;
		}
	}
	swap(array, i, high, size);
	return (i);
}

/**
 * quick_sort_helper - Helper function for the quicksort algorithm
 * @array: Array of integers
 * @low: Starting index of the partition
 * @high: Ending index of the partition
 * @size: The size of the array of integers
 */
void quick_sort_helper(int *array, int low, int high, size_t size)
{
	if (low < high)
	{
		int pivot_index = partition(array, low, high, size);

		quick_sort_helper(array, low, pivot_index - 1, size);
		quick_sort_helper(array, pivot_index + 1, high, size);
	}
}

/**
 * quick_sort - Quicksort algorithm to sort an array of integers
 * @array: Array of integers
 * @size: The size of the array of integers
 */
void quick_sort(int *array, size_t size)
{
	if (array == NULL || size < 2)
	{
		return;
	}
	quick_sort_helper(array, 0, size - 1, size);
}
