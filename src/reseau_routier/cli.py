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


def affiche_analyse_d(max_d: int) -> None:
    """Affiche l'analyse de la capacité de la ville d."""

    capacites_testees = list(range(1, max_d + 1))
    resultats = analyse_impact_capacite_ville(
        reseau=reseau_exemple,
        capacites_villes=capacites_villes_exemple,
        ville="d",
        capacites_testees=capacites_testees,
    )

    print("=== Analyse de la ville d ===")
    print("Capacité de d | Flot maximal")
    print("----------------------------")
    for capacite, flot in resultats.items():
        print(f"{capacite:<13} | {flot}")


def affiche_meilleure_capacite(max_d: int) -> None:
    """Affiche la capacité minimale utile de la ville d."""

    capacite, flot = trouve_capacite_minimale_utile(
        reseau=reseau_exemple,
        capacites_villes=capacites_villes_exemple,
        ville="d",
        capacite_max=max_d,
    )

    print("=== Meilleure capacité pour la ville d ===")
    print(f"Capacité minimale utile : {capacite}")
    print(f"Flot maximal atteint : {flot}")


@app.command()
def exemple() -> None:
    """Résout les questions 1 et 3 sur l'exemple du sujet."""

    affiche_resultats_exemple()


@app.command()
def analyse_d(max_d: int = 10) -> None:
    """Analyse l'impact de la capacité de la ville d."""

    affiche_analyse_d(max_d=max_d)


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

    affiche_analyse_d(max_d=max_d)
    print()

    affiche_meilleure_capacite(max_d=max_d)


if __name__ == "__main__":
    app()
