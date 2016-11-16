import collections
class TreeNode(object):
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None
    def __repr__(self):
        if self:
            serial = []
            queue = [self]
            while queue:
                cur = queue[0]
                if cur:
                    serial.append(cur.data)
                    queue.append(cur.left)
                    queue.append(cur.right)
                else:
                    serial.append("#")
                queue = queue[1:]
            while serial[-1] == "#":
                serial.pop()
            return repr(serial)
        else:
            return None

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
            
    def print_me(self, c_root=None, level = 0):
        if not c_root: c_root = self.root
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

    def is_balanced(self):
        result = 0
        if self.root is not None:
            result = self.is_balanced_helper(self.root)
        if result == -1:
            return False
        return True
  
    def is_balanced_helper(self, c_root):
        if c_root == None:
            return 0
        left = 0
        right = 0
        if c_root.left:
            left = self.is_balanced_helper(c_root.left)
        if c_root.right:
            right = self.is_balanced_helper(c_root.right)
        if left == -1 or right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        else:
            return max(left + 1, right +1)

    def balance(self, c_root):
        if not c_root: return (0, None)
        (l_depth, c_root.left) = self.balance(c_root.left)
        (r_depth, c_root.right) = self.balance(c_root.right)
        l_depth += 1
        r_depth += 1
        if l_depth - r_depth > 1:
            new_root = c_root.left
            c_root.left = c_root.left.right
            new_root.right = c_root
            return (max(r_depth + 1, l_depth - 1), new_root)
        elif l_depth - r_depth < -1:
            new_root = c_root.right
            c_root.right = c_root.right.left
            new_root.left = c_root
            return (max(r_depth - 1, l_depth + 1), new_root)
        else:
            return (max(r_depth, l_depth), c_root)       
        
if __name__=="__main__":
    tree = BinaryTree([x for x in range(31)])
    tree.print_me(tree.root)
    
