from graphviz import Digraph

class TreeNode:
    def __init__(self, digit):
        self.digit = digit
        self.children = [] 

class BinaryTree:
    def __init__(self):
        self.root = None

    # def insert(self, digit):
    #     self.root = self._insert(self.root, digit)


    def insert_digit_by_list(self, digit_list):
        temp = TreeNode(digit_list[0])
        self.root = temp
        #print(temp)
        for i in range(1, len(digit_list)):
            #print(digit_list[i])
            temp = self._insert(temp,digit_list[i])

    def _insert(self, node, digit):
        if node is None:
            return TreeNode(digit)
        newchild = TreeNode(digit)
        #print(newchild)
        #print(f"node: {node}")
        node.children.append(newchild)
        return newchild

    def search(self, digit):
        return self._search(self.root, digit)

    def _search(self, node, digit):
        if node is None or node.digit == digit:
            return node
        for child in node.children:
            if child.digit == digit:
                return child
        return None

class HashMapTree:
    def __init__(self):
        self.hashmap = {}

    def insert_empty_tree(self, key):
        self.hashmap[key] = BinaryTree()


    def insert_digit(self, key, number):
        if key in self.hashmap:
            tree: BinaryTree = self.hashmap[key]
            # #####################
            # for digit in str(number):
            #     tree.insert(int(digit))

            list_of_digits = [int(digit) for digit in str(number)]
            tree.insert_digit_by_list(list_of_digits)
        else:
            print(f"Tree not found for key {key}")


    def search_digit(self, key, digit):
        if key in self.hashmap:
            node = self.hashmap[key].search(digit)
            return node is not None
        else:
            print(f"Tree not found for key {key}")
            return False

    def visualize(self):
        dot = Digraph(comment='HashMapTree')

        for key, tree in self.hashmap.items():
            dot.node(key, key)
            self._visualize_tree(dot, tree.root, key)

        dot.render('hashmap_tree', format='png', cleanup=True)

    def _visualize_tree(self, dot, node, parent_key):
        if node:
            dot.node(f"{parent_key}_{node.digit}", str(node.digit))
            for child in node.children:
                dot.edge(f"{parent_key}_{node.digit}", f"{parent_key}_{child.digit}", label='Child')
                self._visualize_tree(dot, child, parent_key)

# Example usage:
hashmap_tree = HashMapTree()

# Insert empty trees
hashmap_tree.insert_empty_tree("0")
hashmap_tree.insert_empty_tree("1")
# hashmap_tree.insert_empty_tree("2")
# hashmap_tree.insert_empty_tree("3")

# Insert digits into trees
# hashmap_tree.insert_digit("0", 1234761234)
hashmap_tree.insert_digit("0", 456789)
hashmap_tree.insert_digit("1", 456789)
hashmap_tree.visualize()

# for i,j in hashmap_tree.hashmap.items():
#     if j.root is not None:
#         print(j.root.digit)
#         child = j.root.children[0]
#         for i in range(6):
#             print(child.digit)
#             if len(child.children) == 0:
#                 break
#             child = child.children[0]
#     print("")
