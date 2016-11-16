import collections
class StoreNode:
    def __init__(self, node):
        self.Node = None
        
class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None
        self.next = None
        self.parent = None

    def create_ll(self, root):
        q = collections.deque()
        depth = collections.deque()
        q.append(root)
        depth.append(0)
        previous_node = None
        prev_depth = -1
        
        while q:
            cur_node = q.popleft()
            cur_depth = depth.popleft()
            if cur_depth != prev_depth:
                previous_node = cur_node
            else:
                previous_node.next = cur_node
            if cur_node.left:
                q.append(cur_node.left)
                depth.append(cur_depth+1)
            if cur_node.right:
                q.append(cur_node.right)
                depth.append(cur_depth+1)
            previous_node = cur_node
            prev_depth = cur_depth
    def find_inorder_successor(self, root):
        if root.right:
            return root.right
        cur_node = root
        while cur_node.parent:
            if cur_node.parent.left == cur_node:
                return cur_node.parent
            cur_node = cur_node.parent
        return False
    
    def find_common_ancestor(self, root, node1, node2):
        storeNode = StoreNode(1)
        self.find_common_ancestor_helper(root, node1, node2, storeNode)
        return storeNode.Node
    def find_common_ancestor_helper(self, root, node1, node2, storeNode):
        if not root:
            return False
        if root is node1 or root is node2:
            return True
        left = False
        right = False
        if root.left:
            left = self.find_common_ancestor_helper(root.left, node1, node2, storeNode)
        if root.right:
            right = self.find_common_ancestor_helper(root.right, node1, node2, storeNode)
        if left and right:
            storeNode.Node = root
            print(root.data)
            return True
        if left or right: return True
        return False
        

if __name__=="__main__":
    root = Node(10)
    root.left = Node(1)
    root.left.parent = root
    root.right = Node(12)
    root.right.parent = root
    root.left.left = Node(4)
    root.left.left.parent = root.left
    root.left.right = Node(124)
    root.left.right.parent = root.left
    root.right.left = Node(3)
    root.right.left.parent = root.right
    root.right.right = Node(8)
    root.right.right.parent = root.right
    root.create_ll(root)
    print(root.left.left.next)

            
