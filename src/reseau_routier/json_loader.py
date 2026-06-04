import json

from reseau_routier.data import Reseau, Route


def charge_reseau_json(
    chemin: str,
) -> tuple[Reseau, dict[str, int]]:
    """Charge un réseau depuis un fichier JSON."""

    with open(chemin, encoding="utf-8") as fichier:
        donnees = json.load(fichier)

    reseau = Reseau(
        villes=donnees["villes"],
        routes=[
            Route(**route)
            for route in donnees["routes"]
        ],
        source=donnees["source"],
        puits=donnees["puits"],
    )

    return (
        reseau,
        donnees["capacites_villes"],
    )