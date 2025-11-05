def square_large(n):
    if len(n) == 1:
        return str(int(n)*int(n))
    mid = len(n)//2
    left = n[:mid]
    right = n[mid:]
    return str(int(square_large(left)) * (10**(2*(len(n)-mid))) +
               2*int(left)*int(right) * (10**(len(n)-mid)) +
               int(square_large(right)))

num = input("Enter large number: ")
print("Square =", square_large(num))