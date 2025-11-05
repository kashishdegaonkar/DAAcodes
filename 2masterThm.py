def master_theorem(a,b):
    print("Case checking for T(n)=aT(n/b)+n^k")
    if a < b:
        print("Case 1: O(n)")
    elif a == b:
        print("Case 2: O(n log n)")
    else:
        print("Case 3: O(n^log_b(a))")

a = int(input("Enter a: "))
b = int(input("Enter b: "))
master_theorem(a,b)