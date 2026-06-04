"""Description.

Interface en ligne de commande du projet réseau routier.
"""

import typer

from reseau_routier.json_loader import charge_reseau_json
from reseau_routier.flot import (
    analyse_impact_capacite_ville,
    calcule_flot_maximal,
    calcule_flot_maximal_capacites_villes,
    trouve_capacite_minimale_utile,
)

app = typer.Typer()
reseau_exemple, capacites_villes_exemple = ( charge_reseau_json("reseau.json") )

def affiche_resultats_exemple() -> None:
    """Affiche les résultats des questions 1 et 3."""

    flot_simple = calcule_flot_maximal(reseau_exemple)
    flot_villes = calcule_flot_maximal_capacites_villes(
        reseau=reseau_exemple,
        capacites_villes=capacites_villes_exemple,
    )

    print("=== Exemple du sujet ===")
    print(f"Question 1 - flot maximal sans capacités sur les villes : {flot_simple}")
    print(f"Question 3 - flot maximal avec capacités sur les villes : {flot_villes}")


@app.command()
def analyse_ville(
    ville: str,
    capacite_max: int = 10,
) -> None:
    """Analyse l'impact de la capacité d'une ville."""

    capacites_testees = list(range(1, capacite_max + 1))

    resultats = analyse_impact_capacite_ville(
        reseau=reseau_exemple,
        capacites_villes=capacites_villes_exemple,
        ville=ville,
        capacites_testees=capacites_testees,
    )

    print(f"=== Analyse de la ville {ville} ===")
    print("Capacité | Flot maximal")
    print("-----------------------")

    for capacite, flot in resultats.items():
        print(f"{capacite:<8} | {flot}")


@app.command()
def exemple() -> None:
    """Résout les questions 1 et 3 sur l'exemple du sujet."""

    affiche_resultats_exemple()




@app.command()
def meilleure_capacite(
    ville: str = "d",
    capacite_max: int = 20,
) -> None:
    """Recherche la capacité minimale utile pour une ville."""

    capacite, flot = trouve_capacite_minimale_utile(
        reseau=reseau_exemple,
        capacites_villes=capacites_villes_exemple,
        ville=ville,
        capacite_max=capacite_max,
    )

    print("=== Recherche de la meilleure capacité ===")
    print(f"Ville étudiée : {ville}")
    print(f"Capacité minimale utile : {capacite}")
    print(f"Flot maximal atteint : {flot}")


@app.command()
def tout(max_d: int = 10) -> None:
    """Affiche tous les résultats principaux du sujet."""

    affiche_resultats_exemple()
    print()

    analyse_ville(
    ville="d",
    capacite_max=max_d,
)
    print()

    meilleure_capacite(ville="d", capacite_max=max_d)


if __name__ == "__main__":
    app()
