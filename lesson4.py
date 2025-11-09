#Linear Search
# arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
# key = int(input("Enter the key to search for: "))

# if key in arr:
#     print("Element found")

# #Method 1
# for i in range(0, len(arr)):
#     if arr[i] == key:
#         print("Element found at index", i)

# #Method 2
# for i in arr:
#     if i == key:
#         print("Element found")

#Binary Search
# def binary_search(arr, low, high, key):
#     mid = (low + high) // 2
#     if low <= high:
#         if arr[mid] == key:
#             return mid
#         elif arr[mid] > key:
#             return binary_search(arr, low, mid - 1, key)
#         else:
#             return binary_search(arr, mid + 1, high, key)
        
#     else:
#         return -1

# print(binary_search([2, 3, 4, 10, 40], 0, 4, 10))

#Method 2

arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
key = int(input("Enter the key to search for: "))

start = 0
end = len(arr) - 1
found = False

while start <= end:
    mid = (start + end) // 2
    if arr[mid] == key:
        print("Element found at index", mid)
        found = True
        break
    elif arr[mid] < key:
        start = mid + 1
    else:
        end = mid - 1

if found == False:
    print("Element not found")