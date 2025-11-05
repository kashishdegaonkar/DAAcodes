print("---- 3-SAT to Vertex Cover Reduction Demo ----")

# Example 3-SAT formula:
# (x1 OR x2 OR x3) AND (x1 OR x2 OR x3')

clauses = [
    ["x1", "x2", "x3"],
    ["x1", "x2", "¬x3"]
]

# Convert each clause into triangle graph  (conceptual)
graph = []

for clause in clauses:
    print("\nClause:", clause)
    print("Corresponding triangle edges (Vertex Cover gadget):")

    edges = []
    # fully connect clause literals (triangle)
    for i in range(3):
        for j in range(i + 1, 3):
            edges.append((clause[i], clause[j]))

    graph.append(edges)
    for e in edges:
        print(e)

print("\nExplanation:")
print("Each clause becomes a triangle.")
print("Picking one literal per clause gives Vertex Cover selection.")
print("Thus 3-SAT reduces to Vertex Cover in polynomial time.")