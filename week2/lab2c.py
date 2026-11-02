def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


arr = list(map(int, input("Enter elements: ").split()))
key = int(input("Enter element to search: "))

# Check whether the list is sorted
if arr != sorted(arr):
    arr.sort()
    print("List was unsorted, so it is sorted first.")

print("Sorted list:", arr)

result = binary_search(arr, key)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")
