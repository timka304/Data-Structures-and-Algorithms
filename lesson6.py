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

def merge_sort(arr, low, high):
    if low < high:
        mid = (low+high)//2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)
        merge(arr, low, mid, high)

arr = [38, 27, 43, 3, 9, 82, 10, 14]
num = len(arr)

merge_sort(arr, 0, num - 1)

print("Sorted array is:", arr)