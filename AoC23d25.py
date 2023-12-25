import networkx as nx
inputLines = open("input25.txt").readlines()

# Solved with Solution because it's Christmas!
# https://www.youtube.com/watch?v=S_rdenmcsm8
def partA(lines):
    graph = nx.Graph()

    for line in lines:
        l, r = line.split(":")
        for node in r.strip().split():
            graph.add_edge(l, node)
            graph.add_edge(node, l)

    graph.remove_edges_from(nx.minimum_edge_cut(graph))
    groupA, groupB = nx.connected_components(graph)

    return len(groupA) * len(groupB)

def partB(lines):
    return "Press the Button!"

print(partA(inputLines))
print(partB(inputLines))