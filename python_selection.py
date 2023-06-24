#!/usr/bin/python3

if __name__ == "__main__":

    my_list = [19, 48, 99, 71, 13, 52, 96, 73, 86, 7]

    sot = 0
    # Loop through all elements in our list starting at index 0
       
    # Find the smallest number in our unsorted portion of the list

    # Move the smallest number to the start position of unsorted section of list

    # Repeat until there are no more numbers

    for i in range(0, len(my_list)):
        key = my_list[i]
        index = i
        for j in range(i, len(my_list)):            
            if (key > my_list[j]):
                # my_list[i], my_list[j] = my_list[j], my_list[i]
                # print(f"\t{key} is greater than {my_list[j]}")
                key = my_list[j]
                index = j
                sot = 1
        if sot == 1:
            my_list[i], my_list[index] = my_list[index], my_list[i]
            sot = 0
            print(my_list)
