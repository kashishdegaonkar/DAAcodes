import time

def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if arr[j] < arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j]=arr[j+1]
            arr[j+1]=key
            j -= 1

n = int(input("Enter size: "))
arr = list(map(int,input("Enter numbers: ").split()))

for sort,name in [(bubble_sort,"Bubble"),(selection_sort,"Selection"),(insertion_sort,"Insertion")]:
    a = arr.copy()
    start = time.time()
    sort(a)
    end = time.time()
    print(name,"Sort Time =", (end-start))