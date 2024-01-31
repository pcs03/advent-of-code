import networkx as nx
from math import prod

with open("./data/day25.txt", "r") as file:
    G = nx.Graph()
    lines = file.read().splitlines()
    for line in lines:
        source, dests = line.split(": ")
        dests = dests.split()
        G.add_node(source)
        for dest in dests:
            G.add_node(dest)
            G.add_edge(source, dest)
bis = nx.spectral_bisection(G)
print(prod(map(len, bis)))
