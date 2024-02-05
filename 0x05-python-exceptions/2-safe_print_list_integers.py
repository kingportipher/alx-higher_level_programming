#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            # Attempt to access the element at index i
            try:
                # Try to convert the element to an integer
                num = int(my_list[i])
                # If successful, print the integer
                print("{:d}".format(num), end=' ')
                count += 1
            except (ValueError, TypeError):
                # If conversion fails, skip the element silently
                pass
        # Print a new line after printing all integers
        print()
    except IndexError:
        # Handle the case when x is greater than the length of my_list
        print("Exception: x is greater than the length of my_list")
    return count

# Example usage:
my_list = [1, 'a', 2, 'b', 3, 4, 'c']
x = 6
print("Number of integers printed:", safe_print_list_integers(my_list, x))
