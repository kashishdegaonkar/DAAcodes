print("---- Approximation Vertex Cover (Greedy) ----")

edges = [(0,1), (1,2), (2,3), (3,0)]
covered = set()
vertex_cover = set()

for u, v in edges:
    if u not in covered and v not in covered:
        vertex_cover.add(u)
        vertex_cover.add(v)
        covered.add(u)
        covered.add(v)

print("Edges:", edges)
print("Approx Vertex Cover:", vertex_cover)
print("Size =", len(vertex_cover))
print("This is a 2-approximation algorithm.")