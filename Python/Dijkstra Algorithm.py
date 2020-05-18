import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edge('a', 'b', weight=16)
G.add_edge('a', 'c', weight=10)
G.add_edge('a', 'd', weight=5)

G.add_edge('b', 'g', weight=6)
G.add_edge('b', 'f', weight=4)

G.add_edge('c', 'b', weight=2)
G.add_edge('c', 'd', weight=4)
G.add_edge('c', 'f', weight=12)
G.add_edge('c', 'e', weight=10)

G.add_edge('d', 'e', weight=15)

G.add_edge('f', 'g', weight=8)
G.add_edge('f', 'e', weight=3)
G.add_edge('f', 'z', weight=16)

G.add_edge('g', 'z', weight=7)

G.add_edge('e', 'z', weight=5)






pos = nx.spring_layout(G)  # positions for all nodes

labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)





# nodes
#nx.draw_networkx_nodes(G, pos, node_size=700)
color_map = []
for node in G:
    if (node == 'a' or node =='z'):
        color_map.append('red')
    else:
        color_map.append('green')

nx.draw(G, pos, node_color = color_map, node_size=700)

# edges
nx.draw_networkx_edges(G, pos, edgelist=G.edges,
                       width=6)


# labels
nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')




plt.axis('off')
plt.show()




V = list(G.nodes)  #set of graph nodes
s = V[0]  #starting node

w = list(G.edges(data='weight'))  #edge weights

d = dict(G.nodes)  #distance of each node from s node
prev = dict(G.nodes)  #previous nodes

for e in d:
    d.update({e: 100})


d['a'] = 0


Q = dict()  #set of unprocessed nodes (priority queue)

for v in V:
    Q.update({v:100})

Q['a'] = 0
Q = dict(sorted(Q.items(), key=lambda kv: kv[1], reverse=True))
S = list()  #set of processed nodes

fp = list()

while Q:
    u = Q.popitem()
    print('u = ',u,'\n')
    S.append(u[0])

    for v in G[u[0]]:
        print("G[u[0]] = ",G[u[0]])
        if v not in S:
            w_edge = G.get_edge_data(u[0],v)['weight']

            if d[v] > d[u[0]]+w_edge:
                d[v] = d[u[0]] + w_edge
                prev[v] = u[0]
                print("pre Q[v] = ",Q[v])
                Q[v] = d[u[0]] + w_edge
                print("post Q[v] = ", Q[v])

        print('v = ',v, '   Q = ',Q)
        print('')

    print('prev[u[0]] = ',prev[u[0]])
    #final_path.append(prev[u[0]])
    if prev[u[0]]!={}:
        fp.append(prev[u[0]])

    Q = dict(sorted(Q.items(), key=lambda kv: kv[1], reverse=True))
    print('\n\n')

#final path
fp.append('z')
fp = list(dict.fromkeys(fp))
print('final_path = ', fp)


#a-d-c-b-f-e-z




G2 = G.copy()
#print("G2.edges -> ",G2.edges)


elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 0.5]

px = list()
px = [(fp[0],fp[1]),(fp[1],fp[2]),(fp[2],fp[3]),(fp[3],fp[4]),(fp[4],fp[5]),(fp[5],fp[6])]
print("px -> ",px)
rest = G2.edges - px
print("rst -> ", rest)
#print(G.nodes)

#pos2 = nx.spring_layout(G2)  # positions for all nodes

labels = nx.get_edge_attributes(G2,'weight')
nx.draw_networkx_edge_labels(G2,pos,edge_labels=labels)

# nodes
color_map = []
for node in G2:
    if (node == 'a' or node =='z'):
        color_map.append('red')
    else:
        color_map.append('green')

nx.draw(G2, pos, node_color = color_map, node_size=700)


# edges
nx.draw_networkx_edges(G2, pos, edgelist=px,
                       width=6, edge_color='red')

#nx.draw_networkx_edges(G2, pos, edgelist=rest, width=6, edge_color='black')

# labels
nx.draw_networkx_labels(G2, pos, font_size=20, font_family='sans-serif')


plt.axis('off')
plt.show()



