"""Description.

Module de calcul de flot maximal dans un réseau routier.
"""

import networkx as nx
from typing import cast

from reseau_routier.data import Reseau
from reseau_routier.modeles import construit_graphe_capacites_villes


def construit_graphe(reseau: Reseau) -> nx.DiGraph:
    """Construit un graphe orienté networkx à partir d'un réseau."""

    graphe = nx.DiGraph()

    for route in reseau.routes:
        graphe.add_edge(
            route.depart,
            route.arrivee,
            capacity=route.capacite,
        )

    return graphe


def calcule_flot_maximal(reseau: Reseau) -> int:
    """Calcule le flot maximal entre la source et le puits."""

    graphe = construit_graphe(reseau)

    flot, _ = nx.maximum_flow(graphe, reseau.source, reseau.puits, capacity="capacity")

    return cast(int, flot)


def calcule_flot_maximal_capacites_villes(
    reseau: Reseau,
    capacites_villes: dict[str, int],
) -> int:
    """Calcule le flot maximal en tenant compte des capacités sur les villes."""

    graphe = construit_graphe_capacites_villes(
        reseau=reseau,
        capacites_villes=capacites_villes,
    )

    flot, _ = nx.maximum_flow(graphe, reseau.source, reseau.puits, capacity="capacity")

    return cast(int, flot)


def analyse_impact_capacite_ville(
    reseau: Reseau,
    capacites_villes: dict[str, int],
    ville: str,
    capacites_testees: list[int],
) -> dict[int, int]:
    """Analyse l'impact de la capacité d'une ville sur le flot maximal."""

    if ville not in capacites_villes:
        msg = f"La ville {ville} n'a pas de capacité définie"
        raise ValueError(msg)

    resultat = dict()

    for capacite in capacites_testees:
        if capacite <= 0:
            msg = "Les capacités testées doivent être strictement positives"
            raise ValueError(msg)

        nouvelles_capacites = dict(capacites_villes)
        nouvelles_capacites[ville] = capacite

        resultat[capacite] = calcule_flot_maximal_capacites_villes(
            reseau=reseau,
            capacites_villes=nouvelles_capacites,
        )

    return resultat


def trouve_capacite_minimale_utile(
    reseau: Reseau,
    capacites_villes: dict[str, int],
    ville: str,
    capacite_max: int = 20,
) -> tuple[int, int]:
    """Trouve la plus petite capacité utile pour une ville.

    La capacité minimale utile est la plus petite capacité permettant
    d'atteindre le meilleur flot maximal observé.
    Au-delà de cette capacité, augmenter la ville n'améliore plus le flot.
    """

    resultats = analyse_impact_capacite_ville(
        reseau=reseau,
        capacites_villes=capacites_villes,
        ville=ville,
        capacites_testees=list(range(1, capacite_max + 1)),
    )

    flot_max_observe = max(resultats.values())

    for capacite, flot in resultats.items():
        if flot == flot_max_observe:
            return capacite, flot

    raise RuntimeError("Aucune capacité utile trouvée")
