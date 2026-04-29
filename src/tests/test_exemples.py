"""Description.

Tests unitaires de l'exemple du sujet.
"""

from reseau_routier.exemple import reseau_exemple, capacites_villes_exemple
from reseau_routier.flot import (
    calcule_flot_maximal,
    calcule_flot_maximal_capacites_villes,
)


def test_flot_maximal_exemple():
    assert calcule_flot_maximal(reseau_exemple) == 18


def test_flot_maximal_exemple_capacites_villes():
    assert (
        calcule_flot_maximal_capacites_villes(
            reseau_exemple,
            capacites_villes_exemple,
        )
        == 16
    )