
def breadth_search_first(graph, start):
  visited, queue = set(), [start]
  while queue:
    vertex = queue.pop(0)
    if vertex not in visited:
      visited.add(vertex)
      queue.extend(graph[vertex] - visited)
  return visited

graph_1 = {
  'A': set(['B', 'C']),
  'B': set(['A', 'D', 'E']),
  'C': set(['A', 'F']),
  'D': set(['B']),
  'E': set(['B','F']),
  'F': set(['C', 'E'])
}

print(breadth_search_first(graph_1, 'A'))
