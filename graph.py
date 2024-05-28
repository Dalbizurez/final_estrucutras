import graphviz as gv

def tree_g(root):
    graph = gv.Digraph(format='png')
    if root:
        preorder_graph(root, graph) 
    graph.render('img/btree')

def preorder_graph(node, graph : gv.Digraph = None):
    # graph = gv.Digraph(format='png')
    if node:
        graph.node(str(node.key))
        if node.left:
            graph.edge(str(node.key), str(node.left.key))
        preorder_graph(node.left, graph)
        if node.right:
            graph.edge(str(node.key), str(node.right.key))
        preorder_graph(node.right, graph)