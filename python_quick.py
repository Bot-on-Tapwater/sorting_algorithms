#!/usr/bin/python3

if __name__ == "__main__":
    my_list = [19, 48, 99, 71, 13, 52, 96, 73, 86, 50]

    small_list = []
    large_list = []

    # print("Starting programme")

    # Create function that partitions the list

    # The pivot will always be the last element in the list

    # The last element is at index [len(my_list) - 1]

    # Elems smaller than pivot to be moved to the left

    # Elems larger than pivot to be moved to the right

    def partition(my_list):

        key_index = len(my_list) - 1

        key = my_list[key_index]
        
        for elem in my_list:
            if elem < key:
                print(f"\t\tComparing elem: {elem} and key: {key}")
                my_list.insert(key_index, my_list.pop(0))
            else:
                print(f"Comparing elem: {elem} and key: {key}")
                my_list.append(my_list.pop(0))
        
        print(my_list)
    
    partition(my_list)
        



   
