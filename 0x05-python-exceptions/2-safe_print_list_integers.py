#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            try:
                if isinstance(my_list[i], int):
                    print("{:d}".format(my_list[i]), end=' ')
                    count += 1
            except IndexError:
                # Handle the case when x is greater than the length of my_list
                raise Exception("Exception: x is greater than the length of my_list")
    except Exception as e:
        print(e)
    print()
    return count

# Example usage:
my_list = [1, 'a', 2, 'b', 3, 4, 'c']
x = 6
print("Number of integers printed:", safe_print_list_integers(my_list, x))

