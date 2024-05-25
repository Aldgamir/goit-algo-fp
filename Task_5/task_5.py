import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def generate_color(index, total):
    intensity = int(255 * (index / total))
    hex_color = f'#{intensity:02x}{intensity:02x}{255 - intensity:02x}'
    return hex_color

def traverse_and_color(root, traversal_func):
    nodes = traversal_func(root)
    total_nodes = len(nodes)
    for index, node in enumerate(nodes):
        node.color = generate_color(index, total_nodes)
    return root

def depth_first_traversal(root):
    if not root:
        return []
    return [root] + depth_first_traversal(root.left) + depth_first_traversal(root.right)

def breadth_first_traversal(root):
    if not root:
        return []
    queue = [root]
    result = []
    while queue:
        current = queue.pop(0)
        result.append(current)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Обхід в глибину
root_dfs_colored = traverse_and_color(root, depth_first_traversal)
draw_tree(root_dfs_colored)

# Обхід в ширину
root_bfs_colored = traverse_and_color(root, breadth_first_traversal)
draw_tree(root_bfs_colored)
