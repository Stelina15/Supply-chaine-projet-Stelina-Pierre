"""Description.

Tests unitaires du module flot.py
"""

import networkx as nx
import pytest

from reseau_routier.data import Route, Reseau
from reseau_routier.flot import (
    construit_graphe,
    calcule_flot_maximal,
    calcule_flot_maximal_capacites_villes,
    analyse_impact_capacite_ville,
)



def test_construit_graphe_simple():
    reseau = Reseau(
        villes=["E", "a", "S"],
        routes=[
            Route(depart="E", arrivee="a", capacite=5),
            Route(depart="a", arrivee="S", capacite=3),
        ],
        source="E",
        puits="S",
    )

    graphe = construit_graphe(reseau)

    attendu = nx.DiGraph()
    attendu.add_edge("E", "a", capacity=5)
    attendu.add_edge("a", "S", capacity=3)

    assert nx.utils.graphs_equal(graphe, attendu)





def test_flot_maximal_simple():
    reseau = Reseau(
        villes=["E", "a", "S"],
        routes=[
            Route(depart="E", arrivee="a", capacite=5),
            Route(depart="a", arrivee="S", capacite=3),
        ],
        source="E",
        puits="S",
    )

    flot = calcule_flot_maximal(reseau)

    assert flot == 3



def test_flot_maximal_plus_complexe():
    reseau = Reseau(
        villes=["E", "a", "b", "S"],
        routes=[
            Route(depart="E", arrivee="a", capacite=10),
            Route(depart="E", arrivee="b", capacite=5),
            Route(depart="a", arrivee="S", capacite=4),
            Route(depart="b", arrivee="S", capacite=6),
        ],
        source="E",
        puits="S",
    )

    flot = calcule_flot_maximal(reseau)

    assert flot == 9
    




def test_flot_maximal_capacites_villes():
    reseau = Reseau(
        villes=["E", "a", "S"],
        routes=[
            Route(depart="E", arrivee="a", capacite=5),
            Route(depart="a", arrivee="S", capacite=3),
        ],
        source="E",
        puits="S",
    )

    capacites_villes = {"a": 2}

    flot = calcule_flot_maximal_capacites_villes(
        reseau=reseau,
        capacites_villes=capacites_villes,
    )

    assert flot == 2






def test_analyse_impact_capacite_ville():
    reseau = Reseau(
        villes=["E", "a", "S"],
        routes=[
            Route(depart="E", arrivee="a", capacite=5),
            Route(depart="a", arrivee="S", capacite=5),
        ],
        source="E",
        puits="S",
    )

    capacites_villes = {"a": 10}

    resultat = analyse_impact_capacite_ville(
        reseau=reseau,
        capacites_villes=capacites_villes,
        ville="a",
        capacites_testees=[1, 3, 8],
    )

    assert resultat == {
        1: 1,
        3: 3,
        8: 5,
    }








def test_analyse_impact_capacite_ville_invalide():
    reseau = Reseau(
        villes=["E", "a", "S"],
        routes=[
            Route(depart="E", arrivee="a", capacite=5),
            Route(depart="a", arrivee="S", capacite=5),
        ],
        source="E",
        puits="S",
    )

    capacites_villes = {"a": 10}

    with pytest.raises(ValueError):
        analyse_impact_capacite_ville(
            reseau=reseau,
            capacites_villes=capacites_villes,
            ville="b",
            capacites_testees=[1, 2, 3],
        )







def test_analyse_impact_capacite_testee_invalide():
    reseau = Reseau(
        villes=["E", "a", "S"],
        routes=[
            Route(depart="E", arrivee="a", capacite=5),
            Route(depart="a", arrivee="S", capacite=5),
        ],
        source="E",
        puits="S",
    )

    capacites_villes = {"a": 10}

    with pytest.raises(ValueError):
        analyse_impact_capacite_ville(
            reseau=reseau,
            capacites_villes=capacites_villes,
            ville="a",
            capacites_testees=[1, 0, 3],
        )





def test_flot_maximal_capacite_ville_non_limitante():
    reseau = Reseau(
        villes=["E", "a", "S"],
        routes=[
            Route(depart="E", arrivee="a", capacite=5),
            Route(depart="a", arrivee="S", capacite=3),
        ],
        source="E",
        puits="S",
    )

    flot = calcule_flot_maximal_capacites_villes(
        reseau=reseau,
        capacites_villes={"a": 10},
    )

    assert flot == 3