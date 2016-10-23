import collections
class TreeNode(object):
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, array):
        array.sort()
        self.root = self.create_binary_st_helper(array, 0, len(array)-1)
        
    def create_binary_st_helper(self, array, start, end):
        mid = int((start + end) / 2)
        if mid == end:
            # There is only one element
            return TreeNode(array[mid])
        elif mid == start:
            new_node = TreeNode(array[end])
            new_node.left = TreeNode(array[mid])
            return new_node
        else:
            new_node = TreeNode(array[mid])
            new_node.left = self.create_binary_st_helper(array, start, mid-1)
            new_node.right = self.create_binary_st_helper(array, mid+1, end)
            return new_node

    def print_preorder(self, c_root):
        print(c_root.data)
        if (c_root.left): self.print_preorder(c_root.left)
        if (c_root.right): self.print_preorder(c_root.right)
        
    def print_inorder(self, c_root):
        if (c_root.left): self.print_inorder(c_root.left)
        print(c_root.data)
        if (c_root.right): self.print_inorder(c_root.right)
        
    def print_postorder(self, c_root):
        if (c_root.left): self.print_postorder(c_root.left)
        if (c_root.right): self.print_postorder(c_root.right)
        print(c_root.data)
        
    def print_BFS(self, c_root):
        q = collections.deque()
        q.append(c_root)
        while q:
            cur = q.popleft()
            if cur.left: q.append(cur.left)
            if cur.right: q.append(cur.right)
            print (cur.data)
            
    def print_DFS(self, c_root):
        stack = []
        stack.append(c_root)
        while stack:
            cur = stack.pop()
            if cur.right: stack.append(cur.right)
            if cur.left: stack.append(cur.left)
            print(cur.data)
            
    def print_me(self, c_root, level = 0):
        this_level = [c_root]
        print(c_root.data)
        while this_level:
            next_level = list()
            print_array = []
            for n in this_level:
                if n.left:
                    next_level.append(n.left)
                    print_array.append(n.left.data)
                else:
                    print_array.append('-')
                if n.right:
                    next_level.append(n.right)
                    print_array.append(n.right.data)
                else:
                    print_array.append('-')
            this_level = next_level
            print (print_array)
        
    def max_depth(self, c_root):
        depth_l = 1
        depth_r = 1
        if c_root.left:
            depth_l = self.max_depth(c_root.left) + 1
        if c_root.right:
            depth_r = self.max_depth(c_root.right) + 1
        return max(depth_l, depth_r)
        
if __name__=="__main__":
    tree = BinaryTree([x for x in range(31)])
    tree.print_me(tree.root)
    
