"""Description.

Tests unitaires du module modeles.py
"""

import networkx as nx
import pytest

from reseau_routier.data import Route, Reseau
from reseau_routier.modeles import construit_graphe_capacites_villes


def test_construit_graphe_capacites_villes_simple():
    reseau = Reseau(
        villes=["E", "a", "S"],
        routes=[
            Route(depart="E", arrivee="a", capacite=5),
            Route(depart="a", arrivee="S", capacite=3),
        ],
        source="E",
        puits="S",
    )

    graphe = construit_graphe_capacites_villes(
        reseau=reseau,
        capacites_villes={"a": 2},
    )

    attendu = nx.DiGraph()
    attendu.add_node("E")
    attendu.add_node("S")
    attendu.add_edge("E", "a_entree", capacity=5)
    attendu.add_edge("a_entree", "a_sortie", capacity=2)
    attendu.add_edge("a_sortie", "S", capacity=3)

    assert nx.utils.graphs_equal(graphe, attendu)


def test_construit_graphe_capacite_manquante():
    reseau = Reseau(
        villes=["E", "a", "S"],
        routes=[
            Route(depart="E", arrivee="a", capacite=5),
            Route(depart="a", arrivee="S", capacite=3),
        ],
        source="E",
        puits="S",
    )

    with pytest.raises(ValueError):
        construit_graphe_capacites_villes(
            reseau=reseau,
            capacites_villes={},
        )


def test_construit_graphe_ville_inconnue():
    reseau = Reseau(
        villes=["E", "a", "S"],
        routes=[
            Route(depart="E", arrivee="a", capacite=5),
            Route(depart="a", arrivee="S", capacite=3),
        ],
        source="E",
        puits="S",
    )

    with pytest.raises(ValueError):
        construit_graphe_capacites_villes(
            reseau=reseau,
            capacites_villes={"X": 2, "a": 2},
        )


def test_construit_graphe_capacite_invalide():
    reseau = Reseau(
        villes=["E", "a", "S"],
        routes=[
            Route(depart="E", arrivee="a", capacite=5),
            Route(depart="a", arrivee="S", capacite=3),
        ],
        source="E",
        puits="S",
    )

    with pytest.raises(ValueError):
        construit_graphe_capacites_villes(
            reseau=reseau,
            capacites_villes={"a": 0},
        )


def test_flot_avec_capacite_ville_limitante():
    reseau = Reseau(
        villes=["E", "a", "S"],
        routes=[
            Route(depart="E", arrivee="a", capacite=5),
            Route(depart="a", arrivee="S", capacite=3),
        ],
        source="E",
        puits="S",
    )

    graphe = construit_graphe_capacites_villes(
        reseau=reseau,
        capacites_villes={"a": 2},
    )

    flot, _ = nx.maximum_flow(graphe, reseau.source, reseau.puits)

    assert flot == 2