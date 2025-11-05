def binary_search(arr,x):
    l=0; r=len(arr)-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]==x: return mid
        elif arr[mid]<x: l=mid+1
        else: r=mid-1
    return -1

arr=list(map(int,input("Enter sorted numbers: ").split()))
x=int(input("Enter value to search: "))
print("Index =", binary_search(arr,x))
print("Time = O(log n) for sorted, O(n) if unsorted")