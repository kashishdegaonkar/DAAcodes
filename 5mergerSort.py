def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    L=merge_sort(arr[:mid])
    R=merge_sort(arr[mid:])
    i=j=0
    res=[]
    while i<len(L) and j<len(R):
        if L[i]<R[j]: res.append(L[i]);i+=1
        else: res.append(R[j]);j+=1
    res+=L[i:]+R[j:]
    return res

arr=list(map(int,input("Enter numbers: ").split()))
print("Sorted =", merge_sort(arr))
print("Time Complexity = O(n log n)")