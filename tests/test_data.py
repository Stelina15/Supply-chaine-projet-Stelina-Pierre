"""Description.

Tests unitaires du module data.py
"""

from pydantic import ValidationError
import pytest

from reseau_routier.data import Route, Reseau


def test_route_valide():
    route = Route(depart="E", arrivee="a", capacite=5)
    assert route.depart == "E"
    assert route.arrivee == "a"
    assert route.capacite == 5


def test_route_capacite_invalide():
    with pytest.raises(ValidationError):
        Route(depart="E", arrivee="a", capacite=0)


def test_route_boucle():
    with pytest.raises(ValidationError):
        Route(depart="a", arrivee="a", capacite=3)


def test_reseau_valide():
    reseau = Reseau(
        villes=["E", "a", "b", "S"],
        routes=[
            Route(depart="E", arrivee="a", capacite=5),
            Route(depart="a", arrivee="S", capacite=4),
            Route(depart="E", arrivee="b", capacite=3),
        ],
        source="E",
        puits="S",
    )
    assert reseau.source == "E"
    assert reseau.puits == "S"
    assert len(reseau.routes) == 3


def test_reseau_villes_dupliquees():
    with pytest.raises(ValidationError):
        Reseau(
            villes=["E", "a", "a", "S"],
            routes=[],
            source="E",
            puits="S",
        )


def test_reseau_source_invalide():
    with pytest.raises(ValidationError):
        Reseau(
            villes=["E", "a", "S"],
            routes=[],
            source="X",
            puits="S",
        )


def test_reseau_puits_invalide():
    with pytest.raises(ValidationError):
        Reseau(
            villes=["E", "a", "S"],
            routes=[],
            source="E",
            puits="X",
        )


def test_reseau_source_puits_identiques():
    with pytest.raises(ValidationError):
        Reseau(
            villes=["E", "a", "S"],
            routes=[],
            source="E",
            puits="E",
        )


def test_reseau_route_depart_invalide():
    with pytest.raises(ValidationError):
        Reseau(
            villes=["E", "a", "S"],
            routes=[
                Route(depart="X", arrivee="a", capacite=2),
            ],
            source="E",
            puits="S",
        )


def test_reseau_route_arrivee_invalide():
    with pytest.raises(ValidationError):
        Reseau(
            villes=["E", "a", "S"],
            routes=[
                Route(depart="E", arrivee="X", capacite=2),
            ],
            source="E",
            puits="S",
        )


def test_reseau_routes_dupliquees():
    with pytest.raises(ValidationError):
        Reseau(
            villes=["E", "a", "S"],
            routes=[
                Route(depart="E", arrivee="a", capacite=2),
                Route(depart="E", arrivee="a", capacite=5),
            ],
            source="E",
            puits="S",
        )
