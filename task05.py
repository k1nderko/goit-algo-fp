import uuid
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from collections import deque

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.color = "#000000"  
        self.id = str(uuid.uuid4())

def build_tree():
    """ Створення тестового бінарного дерева """
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    return root

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """ Додає вершини та ребра у граф """
    if node:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    """ Візуалізація дерева """
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.clf()  
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors, edge_color="gray")
    plt.pause(0.8)  
    plt.show(block=False)

def generate_colors(n):
    """ Генерує градієнт кольорів від темного до світлого """
    colors = []
    for i in range(n):
        r = int(50 + i * (205 / (n - 1)))
        g = int(80 + i * (175 / (n - 1)))
        b = int(150 + i * (105 / (n - 1)))
        colors.append(f'#{r:02X}{g:02X}{b:02X}')
    return colors

def bfs_visualize(root):
    """ Обхід у ширину (BFS) з візуалізацією кольору """
    if not root:
        return
    
    queue = deque([root])
    nodes = []
    
    while queue:
        node = queue.popleft()
        nodes.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    colors = generate_colors(len(nodes))
    for i, node in enumerate(nodes):
        node.color = colors[i]  
        draw_tree(root)

def dfs_visualize(root):
    """ Обхід у глибину (DFS) з візуалізацією кольору """
    if not root:
        return
    
    stack = [root]
    nodes = []
    
    while stack:
        node = stack.pop()
        nodes.append(node)
        if node.right:  
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    colors = generate_colors(len(nodes))
    for i, node in enumerate(nodes):
        node.color = colors[i] 
        draw_tree(root)

# Побудова дерева
root = build_tree()

print("Обхід у ширину (BFS):")
bfs_visualize(root)

print("Обхід у глибину (DFS):")
dfs_visualize(root)