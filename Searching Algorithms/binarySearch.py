"""
Filename : binarySearch.py
Author : Archit Joshi
Description : Binary Search algorithm implementation. Complexity : O(logn)
Language : python3
Revisions :
v1.0 - Binary search algorithm
"""


def binarySearch(data, find):
    """
    Wrapper function to initiate binary search algorithm.

    :param find: number to find in list
    :param data: sorted list of numbers
    :return: index of search result
    """
    left = 0
    right = len(data)-1

    return _binarySearch(data, left, right, find)


def _binarySearch(data, left, right, element):
    """
    Binary search algorithm. Complexity : O(nlogn)

    :param data: sorted list of numbers
    :param left: leftmost index in current iteration
    :param right: rightmost index in current interation
    :param element: element to search
    :return: index at which element is present , -1 otherwise
    """

    # While search space hasn't been exhausted
    while left <= right:
        # Calculate middle index
        mid = (left + right) // 2

        if data[mid] == element:     # Element found
            return mid
        elif data[mid] < element:    # Recursively search in right half of data
            left = mid + 1
        else:
            right = mid - 1          # Recursively search in left half of data
    return -1


def main():
    # Accept list of numbers and sort the numbers in O(nlogn)
    data = input("Enter list of numbers : ").split()
    data = [int(x) for x in data]
    data = sorted(data)

    # Accept number to be searched
    search = int(input("Enter the number to be searched in data : "))
    print(f"Data : {data}")

    idx = binarySearch(data, search)
    if idx > -1:
        print(f"Number {search} found at index : {idx}")
    else:
        print(f"Element {search} not found in data")


if __name__ == "__main__":
    main()
