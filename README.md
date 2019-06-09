# Python Graph Implementation

Created Graph, Vertex and Edge classes for representing graphs.  
Added an ability to display graph image by using pydot, graphviz and PIL(Python Image Library).

## Example of usage

### Create a graph instance

```python
from graph import Graph
graph = Graph() # Graph(directed=false) for undirected graph
```

### Add vertices

```python
graph.add_vertex("New York")
graph.add_vertex("Bratislava")
graph.add_vertex("Kyiv")
graph.add_vertex("Warsaw")
graph.add_vertex("Atlanta")
```

### Add edges

```python
graph.add_edge("New York", "Bratislava", 7)
graph.add_edge("Bratislava", "Warsaw", 3)
graph.add_edge("Warsaw", "New York", 12)
graph.add_edge("Warsaw", "Kyiv", 5)
graph.add_edge("Kyiv", "Bratislava", 4)
graph.add_edge("Atlanta", "Kyiv", 11)
```

### Remove vertex

```python
graph.remove_vertex("Atlanta")
```

### Remove edge

```python
graph.remove_edge("Atlanta", "Kyiv", 11)
```

### Get all neighbours and edge's weight to them

```python
# get Kyiv vertex and all outbound edges
vertex = graph.get_vertex("Kyiv")
outbound_edges = vertex.get_outbound_edges()

# iterate over outbound edges and get end vertex
for edge in outbound_edges:
  neighbour = edge.get_end_vertex()
  weight = edge.get_weight()
```

### Display graph

```python
from graph import display_graph
display_graph(graph, "Graph name")
```

![Test graph](https://user-images.githubusercontent.com/6642934/59162491-96ebbe80-8afa-11e9-80b9-103cb43db3b3.png)
