"""Description.

Transformations de modèles pour les réseaux routiers.
"""

import networkx as nx

from reseau_routier.data import Reseau


def construit_graphe_capacites_villes(
    reseau: Reseau,
    capacites_villes: dict[str, int],
) -> nx.DiGraph:
    """Construit un graphe tenant compte de capacités sur les villes."""

    graphe = nx.DiGraph()

    villes_internes = [
        ville for ville in reseau.villes if ville not in {reseau.source, reseau.puits}
    ]

    for ville in capacites_villes:
        if ville not in reseau.villes:
            msg = f"Ville inconnue : {ville}"
            raise ValueError(msg)

    for ville in villes_internes:
        if ville not in capacites_villes:
            msg = f"Capacité manquante pour la ville {ville}"
            raise ValueError(msg)
        if capacites_villes[ville] <= 0:
            msg = "Les capacités des villes doivent être strictement positives"
            raise ValueError(msg)

    for ville in reseau.villes:
        if ville in {reseau.source, reseau.puits}:
            graphe.add_node(ville)
        else:
            graphe.add_edge(
                f"{ville}_entree",
                f"{ville}_sortie",
                capacity=capacites_villes[ville],
            )

    for route in reseau.routes:
        depart = route.depart
        arrivee = route.arrivee

        if depart not in {reseau.source, reseau.puits}:
            depart = f"{depart}_sortie"
        if arrivee not in {reseau.source, reseau.puits}:
            arrivee = f"{arrivee}_entree"

        graphe.add_edge(
            depart,
            arrivee,
            capacity=route.capacite,
        )

    return graphe
