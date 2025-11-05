def quick_sort(arr):
    if len(arr)<=1: return arr
    pivot = arr[0]     # first element pivot
    left=[x for x in arr[1:] if x<pivot]
    right=[x for x in arr[1:] if x>=pivot]
    return quick_sort(left)+[pivot]+quick_sort(right)

arr=list(map(int,input("Enter numbers: ").split()))
print("Sorted =", quick_sort(arr))