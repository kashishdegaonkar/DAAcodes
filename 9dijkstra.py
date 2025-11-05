import heapq
def dijkstra(graph,start):
    dist={i:999999 for i in graph}
    dist[start]=0
    pq=[(0,start)]
    while pq:
        d,node=heapq.heappop(pq)
        for nxt,w in graph[node]:
            if d+w < dist[nxt]:
                dist[nxt]=d+w
                heapq.heappush(pq,(dist[nxt],nxt))
    return dist

graph={
1:[(2,2),(3,5)],
2:[(3,1)],
3:[]
}
print("Distances =", dijkstra(graph,1))