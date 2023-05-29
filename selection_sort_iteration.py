def selection_sort(arr):
    n = len(arr)
    count = 0
    for i in range(n-1):
        min_index = 1
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return count

arr = [64,34,25,12,22,11,90]
iterations = selection_sort
print("hasil pengurutan:", arr)
print("jumlah iterasi:", iterations)