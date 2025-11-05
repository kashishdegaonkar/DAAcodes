jobs=[]
n=int(input("Enter number of jobs: "))
for i in range(n):
    p=int(input(f"Profit Job {i+1}: "))
    d=int(input(f"Deadline Job {i+1}: "))
    jobs.append((p,d,i+1))

jobs.sort(reverse=True)

slot=[False]*n
result=[]
for p,d,id in jobs:
    for j in range(min(n,d)-1,-1,-1):
        if slot[j]==False:
            slot[j]=True
            result.append(id)
            break

print("Jobs done =", result)