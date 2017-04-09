# Tutorial: https://www.cl.cam.ac.uk/~cm542/teaching/2010/stna-pdfs/stna-lecture8.pdf

import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Cria um grafo
G = nx.DiGraph()
file_Path = "Base/Amazon0505.txt"


def create_Graph():
    # Abre o arquivo
    with open(file_Path) as fp:
        for line in fp:
            line = line.split()
            # Adiciona um nó ou uma lista de nós
            # G.add_node(1)
            G.add_nodes_from(line)
            # Adiciona arestas entre os nós
            G.add_edge(line[0], line[1])


def analize_Graph():
    file = open("DadosBase.txt", "w")

    # Número de nós
    file.write("Número de Nós: " + str(G.number_of_nodes()))

    # Número de arestas
    file.write("Número de Arestas: " + str(G.number_of_edges()))

    # Componentes Conectadas
    file.write("Número de Componentes Conectadas: " + str(nx.number_strongly_connected_components))
    # print(nx.connected_components(G))

    # Ordena os vértices por grau
    # sorted(nx.degree(G).values())

    # Plota distribuição dos graus
    # Pega o graus de cada vértice:
    in_degrees = G.in_degree()  # dictionary node:degree
    out_degrees = G.out_degree()
    in_values = sorted(set(in_degrees.values()))
    out_values = sorted(set(out_degrees.values()))
    in_hist = Counter(in_degrees.values())
    out_hist = Counter(out_degrees.values())
    plt.figure()
    plt.grid(True)
    plt.plot(in_values, in_hist, 'ro-')  # in-degree
    plt.plot(out_values, out_hist, 'bv-')  # out-degree
    plt.legend(['In-degree', 'Out-degree'])
    plt.xlabel('Degree')
    plt.ylabel('Number of nodes')
    plt.title('network of places in Cambridge')
    # plt.xlim([0, 2*10**2])
    plt.savefig("DistribuicaoDosGraus.pdf")
    plt.close()

    # x = pd.Series(nx.degree(G), name="Distribuição dos Graus dos Nsós")
    # x.savefig("DistribuicaoDosGraus.pdf")

    # #Medida de clusterização
    # print(nx.clustering(G))
    #
    # #Closeness
    # #https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.algorithms.centrality.closeness_centrality.html
    # print(closeness_centrality(G, u=None, distance=None, normalized=True))
    #
    # #Betweenness
    # #https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.algorithms.centrality.betweenness_centrality.html#networkx.algorithms.centrality.betweenness_centrality
    # print(betweenness_centrality(G, k=None, normalized=True, weight=None, endpoints=False, seed=None))
    #
    # #Diameter
    # #https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.algorithms.distance_measures.diameter.html?highlight=diameter
    # print(diameter(G, e=None))
    #
    # #Eccentricity
    # #https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.algorithms.distance_measures.eccentricity.html#networkx.algorithms.distance_measures.eccentricity
    # print(eccentricity(G, v=None, sp=None))
    #
    # #Degree_centrality
    # #https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.algorithms.centrality.degree_centrality.html#networkx.algorithms.centrality.degree_centrality
    # print(degree_centrality(G))


    file.close()


create_Graph()
analize_Graph()

# Limpa todo o grafo
G.clear()