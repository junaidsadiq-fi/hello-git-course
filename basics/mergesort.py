def debug_print(debug_msg=None, **kwargs):
    if debug_msg:
        print(debug_msg)
    for key, value in kwargs.items():
        print("{}: {}".format(key, value))

def mergesort(array, depth=0):
    indent = "  " * depth  # For better readability of debug output
    if len(array) <= 1:
        return array

    m = len(array) // 2
    debug_print(debug_msg=indent + "array:", array=array[:m], m=m)  # Debug left split
    left = mergesort(array[:m], depth + 1)
    
    debug_print(debug_msg=indent + "array:", array=array[m:], m=m)  # Debug right split
    right = mergesort(array[m:], depth + 1)

    merged = merge(left, right)
    debug_print(debug_msg=indent + "Merging...", left=left, right=right, merged=merged)
    return merged

def merge(left, right):
    debug_print(debug_msg="Merging...", left=left, right=right)
    merged = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    merged += left if len(left) > 0 else right
    debug_print(debug_msg="merged:", merged=merged)
    return merged

if __name__ == "__main__":
    input_str = input("Enter numbers, separated by ',': ")
    input_list = input_str.split(",")
    print("input_list:", input_list)  # Print initial input list

    value_list = []
    for x in input_list:
        try:
            value_list.append(int(x))
        except ValueError as err:
            print("Invalid input.")
            quit(1)

    print("value_list:", value_list)  # Print value list after conversion to integers

    sorted_list = mergesort(value_list)
    print(sorted_list)  # Print final sorted list
