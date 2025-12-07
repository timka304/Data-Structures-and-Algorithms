#merge sort numbers
def merge(arr, low, mid, high):
    list = []
    start = low
    start2 = mid + 1

    while start <= mid and start2 <= high:
        if arr[start] < arr[start2]:
            list.append(arr[start])
            start += 1
        else:
            list.append(arr[start2])
            start2 += 1

    while start <= mid:
        list.append(arr[start])
        start += 1

    while start2 <= high:
        list.append(arr[start2])
        start2 += 1
    
    c = 0
    for i in range(low, high + 1):
        arr[i] = list[c]
        c += 1



arr = [38, 27, 43, 3, 9, 82, 10, 14]

a = merge(arr, 0, 3, 7)

print("Sorted array is:", a)