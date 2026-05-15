"""Description.

Interface en ligne de commande du projet réseau routier.
"""

import typer

from reseau_routier.exemple import capacites_villes_exemple, reseau_exemple
from reseau_routier.flot import (
    analyse_impact_capacite_ville,
    calcule_flot_maximal,
    calcule_flot_maximal_capacites_villes,
)

app = typer.Typer()


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


@app.command()
def exemple() -> None:
    """Résout les questions 1 et 3 sur l'exemple du sujet."""

    affiche_resultats_exemple()


@app.command()
def analyse_d(max_d: int = 10) -> None:
    """Analyse l'impact de la capacité de la ville d."""

    affiche_analyse_d(max_d=max_d)


@app.command()
def tout(max_d: int = 10) -> None:
    """Affiche tous les résultats principaux du sujet."""

    affiche_resultats_exemple()
    print()
    affiche_analyse_d(max_d=max_d)


if __name__ == "__main__":
    app()