


from reseau_routier.exemple import reseau_exemple, capacites_villes_exemple
from reseau_routier.flot import (
    calcule_flot_maximal,
    calcule_flot_maximal_capacites_villes,
)
from reseau_routier.modeles import construit_graphe_capacites_villes
from reseau_routier.visugraphe import affiche_graphe





def main() -> None:
    print("=== PROJET RESEAU ROUTIER ===")
    print()

    print("QUESTION 1")
    flot_simple = calcule_flot_maximal(reseau_exemple)
    print("Flot maximal sans capacites sur les villes :", flot_simple)
    print()

    print("QUESTION 3")
    flot_villes = calcule_flot_maximal_capacites_villes(
        reseau_exemple,
        capacites_villes_exemple,
    )
    print("Flot maximal avec capacites sur les villes :", flot_villes)
    print()

    print("QUESTION 4")
    for capacite in range(1, 11):
        nouvelles_capacites = dict(capacites_villes_exemple)
        nouvelles_capacites["d"] = capacite

        flot = calcule_flot_maximal_capacites_villes(
            reseau_exemple,
            nouvelles_capacites,
        )
        print(f"Capacite de d = {capacite} -> flot maximal = {flot}")

    print()
    print("Affichage du graphe transforme de la question 3...")
    graphe = construit_graphe_capacites_villes(
        reseau_exemple,
        capacites_villes_exemple,
    )
    affiche_graphe(graphe)


if __name__ == "__main__":
    main()