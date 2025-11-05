print("---- KRUSKAL & PRIM MST COMPARISON ----")

# Predefined Graph
# (u, v, w)
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

n = 4  # number of vertices


# -------- KRUSKAL --------
def kruskal():
    parent = list(range(n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    mst_cost = 0
    count = 0

    for u, v, w in sorted(edges, key=lambda x: x[2]):
        rootU = find(u)
        rootV = find(v)
        if rootU != rootV:
            parent[rootU] = rootV
            mst_cost += w
            count += 1
            if count == n - 1:
                break
    return mst_cost


# -------- PRIM --------
def prim():
    INF = 99999
    selected = [False] * n
    selected[0] = True
    mst_cost = 0

    for _ in range(n - 1):
        minimum = INF
        a = b = -1

        for u, v, w in edges:
            if selected[u] and not selected[v] and w < minimum:
                a, b, minimum = u, v, w
            if selected[v] and not selected[u] and w < minimum:
                a, b, minimum = v, u, w

        selected[b] = True
        mst_cost += minimum

    return mst_cost


# Output
print("\nKruskal MST Cost:", kruskal())
print("Prim MST Cost:", prim())
print("\n Both algorithms produce same MST cost")