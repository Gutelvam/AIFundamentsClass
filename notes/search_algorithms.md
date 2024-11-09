# Fundaments of AI
## Search algorithms

### Breadth First Search (BFS) 

Breadth First Search (BFS) is a fundamental graph traversal algorithm. It begins with a node, then first traverses all its adjacent. Once all adjacent are visited, then their adjacent are traversed. This is different from DFS in a way that closest vertices are visited before others. We mainly traverse vertices level by level. A lot of popular graph algorithms like Dijkstra’s shortest path, Kahn’s Algorithm, and Prim’s algorithm are based on BFS. BFS itself can be used to detect cycle in a directed and undirected graph, find shortest path in an unweighted graph and many more problems.

### Depth First Traversal (DFS)

Depth First Traversal (or DFS) for a graph is similar to Depth First Traversal of a tree. Like trees, we traverse all adjacent vertices one by one. When we traverse an adjacent vertex, we completely finish the traversal of all vertices reachable through that adjacent vertex. After we finish traversing one adjacent vertex and its reachable vertices, we move to the next adjacent vertex and repeat the process. This is similar to a tree, where we first completely traverse the left subtree and then move to the right subtree. The key difference is that, unlike trees, graphs may contain cycles (a node may be visited more than once). To avoid processing a node multiple times, we use a boolean visited array.

### Depth Limited Search (DLS)

Depth Limited Search is a key algorithm used in the problem space among the strategies concerned with artificial intelligence. The article provides a comprehensive overview of the Depth-Limited Search (DLS) algorithm, explaining its concept, applications, and implementation in solving pathfinding problems in robotics, while also addressing frequently asked questions.

### Uniform Cost Search (UCS)

Uniform Cost Search is a pathfinding algorithm that expands the least cost node first, ensuring that the path to the goal node has the minimum cost. Unlike other search algorithms like Breadth-First Search (BFS), UCS takes into account the cost of each path, making it suitable for weighted graphs where each edge has a different cost.