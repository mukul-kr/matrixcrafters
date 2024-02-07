from collections import deque
from typing import List
from src.data_structure.tree_node import TreeNode


class BinaryTree:
    def __init__(self):
        self.root = None
        self._string = ""

    def to_dict(self):
        return self.root.to_dict() if self.root else None

    def insert_digit_by_list(self, digit_list):
        self._insert(self.root, digit_list, 0)

    def _insert(self, node, digit_list, idx=0):
        if idx >= len(digit_list):
            return node
        if node is not None:
            for i in node.children:
                if i.digit == digit_list[idx]:
                    return self._insert(i, digit_list, idx + 1)
        # check if idx 0 is digit which is already present as value of root
        if idx == 0 and node is not None and node.digit == digit_list[idx]:
            return self._insert(node, digit_list, idx + 1)
        if node is None:
            newchild = TreeNode(-1)
            self.root = newchild
            return self._insert(newchild, digit_list, idx)

        else:
            newchild = TreeNode(digit_list[idx])
            # node.children.append(newchild)
            node.children.append(newchild)
            node.children.sort(key=lambda x: x.digit)
            return self._insert(newchild, digit_list, idx + 1)
        

    def insert_individual_digit(self, node, digit):
        if self.root is None:
            self.root = TreeNode(-1)
            return self.root
        else:
            return self._insert_individual(node, digit)

    """
    dummy logic for inserting individual digit in the tree
    """

    def _insert_individual(self, node, digit):
        if node is None and self.root is None:
                raise ValueError("Tree is empty")
        else:
            new_node = TreeNode(digit)
            node.children.append(new_node)
            node.children.sort(key=lambda x: x.digit)
            return new_node





    def search(self, digit_list):
        return self._search(self.root, digit_list)

    def _search(self, node, digit_list, idx=0):
        if idx >= len(digit_list) or node is None:
            return False
        if node.digit == digit_list[idx]:
            if idx == len(digit_list) - 1:
                return True
            for child in node.children:
                if self._search(child, digit_list, idx + 1):
                    return True
        return False
    

    def bfs(self) -> List[List[List[int]]]:
        if self.root is None:
            return [[[]]]
        queue = deque([(self.root, 1)]) # Add level information to each node
        list_tree :  List[List[List[int]]] = [[],[],[],[],[],[]]
        while len(queue) > 0:
            node, level = queue.popleft() # Get the node and its level
            children = [] # Temporary list to store children
            if node != self.root: # Check if the node is not the root
                print(f"Node: {node.digit}, Level: {level}") # Process the node and its level
            for child in node.children:
                queue.append((child, level + 1)) # Enqueue children with their correct level
                children.append(child.digit) # Store children digits
            if children: # If there were any children
                list_tree[level-1].append(children) # type: ignore # Store children digits
                # print(f"Children: {children}") 
        for i in list_tree:
            print(i)
        return list_tree

    def create_data_to_save(self):
        bfs_traversal_data = self.bfs()

        string_data = ""
        for level_i in bfs_traversal_data:
            for i in level_i:
                array = [0,0,0,0,0,0,0,0,0,0]
                for j in i:
                    array[j] = 1
                string_data += "".join(str(e) for e in array)
            # string_data += "\n"

        return string_data
