import matplotlib.pyplot as plt
import networkx as nx


def affiche_graphe(graphe) -> None:
    """Affiche un graphe avec ses capacités sur les arêtes."""
    
    
    
    positions = nx.spring_layout(graphe)

    _, rep = plt.subplots(figsize=(14, 8))
    nx.draw_networkx_nodes(graphe, pos=positions, ax=rep)
    nx.draw_networkx_edges(graphe, pos=positions, ax=rep)
    nx.draw_networkx_labels(graphe, pos=positions, ax=rep, font_size=9)
    nx.draw_networkx_edge_labels(
        graphe,
        pos=positions,
        edge_labels={
            (depart, arrivee): capacite
            for (depart, arrivee, capacite) in graphe.edges(data="capacity")
        },
        ax=rep,
        font_size=8,
    )
    rep.set_title("Graphe transforme avec capacites sur les villes")
    plt.show()