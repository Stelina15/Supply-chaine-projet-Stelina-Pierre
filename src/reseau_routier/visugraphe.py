"""Description.

Fonctions d'affichage des graphes du projet.
"""

import matplotlib.pyplot as plt
import networkx as nx


def affiche_graphe(graphe: nx.DiGraph) -> None:
    """Affiche un graphe avec ses capacités sur les arêtes."""

    positions = nx.spring_layout(graphe)

    fig, ax = plt.subplots(figsize=(14, 8))

    nx.draw_networkx_nodes(graphe, pos=positions, ax=ax)
    nx.draw_networkx_edges(graphe, pos=positions, ax=ax)
    nx.draw_networkx_labels(graphe, pos=positions, ax=ax, font_size=9)

    nx.draw_networkx_edge_labels(
        graphe,
        pos=positions,
        edge_labels={
            (depart, arrivee): capacite
            for (depart, arrivee, capacite) in graphe.edges(data="capacity")
        },
        ax=ax,
        font_size=8,
    )

    ax.set_title("Graphe du réseau routier")

    plt.show()
