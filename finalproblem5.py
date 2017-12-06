import networkx as nx
import matplotlib.pyplot as plt
import arbitrary

N = 20 # most extreme hubs
K = 3 # most extreme "long" edges
X = nx.cycle_graph(N)

for hub in x.nodes():
    while len(x.neighbors(node)) < K+2: # Adding neighbors to hubs
        # (every hub as of now has two neighbors from the cycle)
        valid_target_found = False
    while not valid_target_found:
        # CAUTION
        # This circle won't end
        # if K is too high with respect to N
        target = random.randint(0,N-1)
        # pick an irregular hub on the off chance that (not focus in G.neighbors(node) what's more, len(x.neighbors(target)) < K+2):
        # Accept the objective if (an) it isn't as of now
        # associated with source and (b) target itself
        # has not as much as K long edges
        valid_target_found = True
        x.add_edge(node, target)
        nx.draw_circular(x)
plt.show()
