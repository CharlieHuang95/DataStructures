import collections
hi = []
class Node:
    def __init__(self, d):
        self.data = d
        self.adjacent = []
        self.visited = False
        
    def connect(self, node):
        self.adjacent.append(node)
        node.adjacent.append(self)

    def connect_undirected(self, node):
        self.adjacent.append(node)

class Graph:
    def __init__(self):
        self.nodes = []

    def reset(self):
        for node in self.nodes:
            node.visited = False
        
    def recurse_DFS(self, node):
        print(node.data)
        node.visited = True
        self.recurse_DFS_helper(node)        
        self.reset()

    def recurse_DFS_helper(self, node):
        for adjacent in node.adjacent:
            if adjacent.visited:
                continue
            adjacent.visited = True
            print(adjacent.data)
            hi.append(adjacent.data)
            self.recurse_DFS_helper(adjacent)

    def BFS(self, node): 
        q = collections.deque()
        q.append(node)
        while q:
            cur_node = q.popleft()
            print(cur_node.data)
            cur_node.visited = True
            for adjacent in cur_node.adjacent:
                if not adjacent.visited: q.append(adjacent)
        self.reset()

    def path_between_two_nodes(self, node1, node2):
        q = collections.deque()
        if node1 == node2: return True
        q.append(node1)
        while q is not None:
            cur_node = q.popleft()
            cur_node.visited = True
            for adjacent in cur_node.adjacent:
                if adjacent.visited:
                    continue
                if adjacent == node2:
                    return True
                q.append(adjacent)
        return False
        self.reset()
                
if __name__=="__main__":
    graph = Graph()
    v1 = Node(3)
    v2 = Node(4)
    v3 = Node(10)
    v4 = Node(12)
    v5 = Node(5)
    v6 = Node(100)
    graph.nodes.append(v1)
    graph.nodes.append(v2)
    graph.nodes.append(v3)
    graph.nodes.append(v4)
    graph.nodes.append(v5)
    graph.nodes.append(v6)
    v3.connect(v2)
    v2.connect(v1)
    v4.connect(v3)
    v5.connect(v4)
    graph.recurse_DFS(v2)
