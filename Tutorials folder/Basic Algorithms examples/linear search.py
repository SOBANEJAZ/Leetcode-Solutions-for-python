def linear_search(list, target):
    # Returns the index position of the target if found, else returns None

    for item in range(0, len(list)):
        if list[item] == target:
            return item
    return None

def verify(index):
    if index is not None:
        print(f"Target found at index {index}")
    else:
        print(f"Target not found in list")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = linear_search(numbers, 10)
verify(result)