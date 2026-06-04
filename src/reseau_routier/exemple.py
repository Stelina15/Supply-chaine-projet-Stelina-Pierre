"""Description.

Exemple de réseau routier issu du sujet.
"""

from reseau_routier.data import Reseau, Route


reseau_exemple = Reseau(
    villes=["E", "a", "b", "c", "d", "e", "f", "g", "S"],
    routes=[
        Route(depart="E", arrivee="a", capacite=5),
        Route(depart="E", arrivee="b", capacite=10),
        Route(depart="E", arrivee="e", capacite=8),
        Route(depart="a", arrivee="c", capacite=7),
        Route(depart="a", arrivee="d", capacite=10),
        Route(depart="b", arrivee="c", capacite=8),
        Route(depart="b", arrivee="d", capacite=2),
        Route(depart="b", arrivee="e", capacite=1),
        Route(depart="c", arrivee="g", capacite=7),
        Route(depart="d", arrivee="g", capacite=4),
        Route(depart="d", arrivee="S", capacite=6),
        Route(depart="d", arrivee="f", capacite=2),
        Route(depart="e", arrivee="f", capacite=4),
        Route(depart="f", arrivee="S", capacite=6),
        Route(depart="g", arrivee="S", capacite=10),
    ],
    source="E",
    puits="S",
)


capacites_villes_exemple = {
    "a": 6,
    "b": 7,
    "c": 8,
    "d": 6,
    "e": 6,
    "f": 5,
    "g": 9,
}
