INF=9999
n=int(input("Enter nodes: "))
g=[]
print("Enter matrix:")
for i in range(n):
    g.append(list(map(int,input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            g[i][j]=min(g[i][j],g[i][k]+g[k][j])

print("Shortest distances:")
for row in g: print(row)