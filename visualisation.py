import marimo

app = marimo.App(width="medium")




@app.cell
def _():
    import marimo as mo
    import matplotlib.pyplot as plt
    import networkx as nx

    from reseau_routier.exemple import reseau_exemple, capacites_villes_exemple
    from reseau_routier.flot import (
        construit_graphe,
        calcule_flot_maximal,
        calcule_flot_maximal_capacites_villes,
    )
    from reseau_routier.modeles import construit_graphe_capacites_villes

    return (
        mo,
        plt,
        nx,
        reseau_exemple,
        capacites_villes_exemple,
        construit_graphe,
        calcule_flot_maximal,
        calcule_flot_maximal_capacites_villes,
        construit_graphe_capacites_villes,
    )





@app.cell
def _(construit_graphe, reseau_exemple):
    graphe_q1 = construit_graphe(reseau_exemple)
    return (graphe_q1,)


@app.cell
def _(calcule_flot_maximal, reseau_exemple):
    flot_q1 = calcule_flot_maximal(reseau_exemple)
    return (flot_q1,)


@app.cell
def _(graphe_q1, nx, plt):
    _positions_q1 = {
        "E": (0, 0),
        "a": (1, 1.2),
        "b": (1, 0),
        "e": (1, -1.2),
        "c": (2.4, 1.4),
        "d": (2.2, 0),
        "f": (3.0, -1.2),
        "g": (3.6, 1.0),
        "S": (4.4, 0),
    }

    fig_q1, ax_q1 = plt.subplots(figsize=(10, 6))

    nx.draw_networkx_nodes(graphe_q1, pos=_positions_q1, ax=ax_q1)
    nx.draw_networkx_edges(graphe_q1, pos=_positions_q1, ax=ax_q1)
    nx.draw_networkx_labels(graphe_q1, pos=_positions_q1, ax=ax_q1, font_size=9)
    nx.draw_networkx_edge_labels(
        graphe_q1,
        pos=_positions_q1,
        edge_labels={
            (_depart, _arrivee): _capacite
            for (_depart, _arrivee, _capacite) in graphe_q1.edges(data="capacity")
        },
        ax=ax_q1,
        font_size=8,
    )

    ax_q1.set_title("Graphe initial du réseau routier")
    plt.close(fig_q1)
    return (fig_q1,)

@app.cell
def _(
    construit_graphe_capacites_villes,
    reseau_exemple,
    capacites_villes_exemple,
):
    graphe_q3 = construit_graphe_capacites_villes(
        reseau_exemple,
        capacites_villes_exemple,
    )
    return (graphe_q3,)


@app.cell
def _(
    calcule_flot_maximal_capacites_villes,
    reseau_exemple,
    capacites_villes_exemple,
):
    flot_q3 = calcule_flot_maximal_capacites_villes(
        reseau_exemple,
        capacites_villes_exemple,
    )
    return (flot_q3,)


@app.cell
def _(graphe_q3, nx, plt):
    _positions_q3 = {
        "E": (0, 0),

        "a_entree": (1, 1.2),
        "a_sortie": (1.4, 1.2),

        "b_entree": (1, 0),
        "b_sortie": (1.4, 0),

        "e_entree": (1, -1.2),
        "e_sortie": (1.4, -1.2),

        "c_entree": (2.4, 1.4),
        "c_sortie": (2.8, 1.4),

        "d_entree": (2.4, 0),
        "d_sortie": (2.8, 0),

        "f_entree": (3.2, -1.2),
        "f_sortie": (3.6, -1.2),

        "g_entree": (3.7, 1.0),
        "g_sortie": (4.1, 1.0),

        "S": (4.8, 0),
    }

    fig_q3, ax_q3 = plt.subplots(figsize=(10, 6))

    nx.draw_networkx_nodes(graphe_q3, pos=_positions_q3, ax=ax_q3)
    nx.draw_networkx_edges(graphe_q3, pos=_positions_q3, ax=ax_q3)
    nx.draw_networkx_labels(graphe_q3, pos=_positions_q3, ax=ax_q3, font_size=8)
    nx.draw_networkx_edge_labels(
        graphe_q3,
        pos=_positions_q3,
        edge_labels={
            (_depart, _arrivee): _capacite
            for (_depart, _arrivee, _capacite) in graphe_q3.edges(data="capacity")
        },
        ax=ax_q3,
        font_size=7,
    )

    ax_q3.set_title("Graphe transformé avec capacités sur les villes")
    plt.close(fig_q3)
    return (fig_q3,)


@app.cell
def _(
    calcule_flot_maximal_capacites_villes,
    reseau_exemple,
    capacites_villes_exemple,
):
    resultats_q4 = {}

    for _capacite in range(1, 11):
        _nouvelles_capacites = dict(capacites_villes_exemple)
        _nouvelles_capacites["d"] = _capacite

        _flot = calcule_flot_maximal_capacites_villes(
            reseau_exemple,
            _nouvelles_capacites,
        )

        resultats_q4[_capacite] = _flot

    return (resultats_q4,)


@app.cell
def _(mo):
    capacite_d = mo.ui.slider(
        start=1,
        stop=10,
        value=6,
        label="Capacité de la ville d",
    )
    return (capacite_d,)


@app.cell
def _(
    capacite_d,
    calcule_flot_maximal_capacites_villes,
    reseau_exemple,
    capacites_villes_exemple,
):
    capacites_modifiees_q4 = dict(capacites_villes_exemple)
    capacites_modifiees_q4["d"] = capacite_d.value

    flot_interactif_q4 = calcule_flot_maximal_capacites_villes(
        reseau_exemple,
        capacites_modifiees_q4,
    )

    return (flot_interactif_q4,)


@app.cell
def _(resultats_q4):
    lignes_tableau_q4 = "\n".join(
        f"| {_capacite} | {_flot} |"
        for _capacite, _flot in resultats_q4.items()
    )

    tableau_q4 = f"""
| Capacité de d | Flot maximal |
|---:|---:|
{lignes_tableau_q4}
"""
    return (tableau_q4,)


@app.cell
def _(resultats_q4, plt):
    capacites = list(resultats_q4.keys())
    flots = list(resultats_q4.values())

    fig_q4, ax_q4 = plt.subplots(figsize=(7, 4))

    ax_q4.plot(capacites, flots, marker="o")
    ax_q4.set_xlabel("Capacité de la ville d")
    ax_q4.set_ylabel("Flot maximal")
    ax_q4.set_title("Influence de la capacité de d sur le flot maximal")
    ax_q4.grid()

    return (fig_q4,)


@app.cell
def _(
    mo,
    flot_q1,
    flot_q3,
    fig_q1,
    fig_q3,
    fig_q4,
    capacite_d,
    flot_interactif_q4,
    tableau_q4,
):
    dashboard = mo.ui.tabs(
        {
            "Accueil": mo.md(
                """
# Exploration du réseau routier

Ce dashboard présente les résultats principaux du projet.

L'objectif est d'étudier un problème de flot maximal dans un réseau routier.

## Organisation

- Question 1 : Quel est le débit horaire maximal de véhicules reliant E à S ? 
- Question 3 : Quel est le nouveau débit horaire maximal de véhicules reliant E à S après ajout des capacités sur les villes ?
- Question 4 : Analyse de la variation du flux total en fonction de la variation du flux maximal traversant d ?


## Démarche pour réaliser ce projet 

Ce projet consiste à étudier un problème de circulation dans un réseau routier à l'aide des outils de théorie des graphes.

Le réseau est modélisé sous forme de graphe orienté, où les sommets représentent des villes et les arêtes représentent des routes.  
Chaque route possède une capacité, qui correspond au nombre maximal de véhicules pouvant y circuler.

Dans un premier temps, on construit ce réseau en Python et on le représente sous forme de graphe à l'aide de la bibliothèque `networkx`.  
On utilise ensuite un algorithme de flot maximal pour déterminer la quantité maximale de flux pouvant être envoyée d'une source `E` vers un puits `S`, en respectant les capacités des routes.

Dans un second temps, on rend le modèle plus réaliste en introduisant des contraintes sur les villes.  
En effet, une ville ne peut pas laisser passer un flux illimité.  
Pour modéliser cela, chaque ville est transformée en deux sommets (`entrée` et `sortie`), reliés par une arête dont la capacité correspond à la capacité maximale de la ville.  
Cette transformation permet d'intégrer les contraintes sur les sommets dans un modèle de flot.

Enfin, on réalise une analyse du fonctionnement du réseau en faisant varier certains paramètres.  
En particulier, on étudie l'influence de la capacité d'une ville sur le flot maximal, afin d'identifier les éléments qui limitent la circulation.

L'objectif de ce travail est de comprendre comment les contraintes locales (routes ou villes) influencent la capacité globale du réseau, et d'identifier les points critiques qui limitent le flux.


"""
            ),
            "Question 1": mo.vstack(
                [
                    mo.md(
                        f"""
# Question 1

Quel est le débit horaire maximal de véhicules reliant E à S ?

Ici on cherche donc à comprendre la capacité globale du réseau routier.
On cherche à savoir quelle quantité maximale de flux peut partir de la source E et arriver
au puits S, en respectant les capacités imposés sur les routes.
On va donc essayer de trouver le flot maximal.  

Résultat :
Le flot maximal vaut est de **{flot_q1}**

## Graphe initial :
"""
                    ),
                    fig_q1,
                    mo.md(
                        """
## Interprétation
Le flot maximal obtenu est de 18.
Cela signifie que le réseau peut transporter au maximum 18 unités de flux de la source E vers le puits S, en respectant les capacités des routes.
Ce résultat montre que le réseau est limité par certaines routes critiques qui atteignent leur capacité maximale. Ces routes constituent des goulots d'étranglement, car elles empêchent d’augmenter davantage le flux global.
Ainsi, le flot maximal dépend de la structure globale du réseau et de la répartition des capacités, et non uniquement des routes ayant les plus grandes capacités.
"""
                    ),
                ]
            ),
            "Question 3": mo.vstack(
                [
                    mo.md(
                        f"""
# Question 3

## Modélisation avec capacités sur les villes

On ajoute maintenant des capacités sur les villes intermédiaires.
En réalité, une ville ne peut pas laisser passer un flux illimité : elle a une capacité maximale.  
Il faut donc intégrer cette contrainte dans le modèle.
Pour cela, chaque ville intermédiaire est transformée en deux sommets :
- `ville_entree`
- `ville_sortie`

Ces deux sommets sont reliés par une arête dont la capacité correspond à la capacité maximale de la ville.
Toutes les routes arrivant dans la ville sont connectées à `ville_entree`, et toutes celles qui en partent sont reliées à `ville_sortie`.
Cette transformation permet de prendre en compte les contraintes sur les villes tout en utilisant les algorithmes classiques de flot maximal, qui fonctionnent uniquement sur les arêtes.


Résultat : Le flot maximal avec capacités sur les villes est de **{flot_q3}**

## Graphe transformé
"""
                    ),
                    fig_q3,
                    mo.md(
                        """
## Interprétation

Le flot maximal obtenu avec les capacités sur les villes est de 16.
On observe une diminution du flot maximal par rapport à la question 1 (où il était de 18).  
Cela s'explique par l'ajout de contraintes supplémentaires : certaines villes limitent désormais le flux pouvant les traverser.
Ces villes jouent un rôle de goulot d'étranglement, car même si les routes ont encore de la capacité disponible, le flux total est bloqué par la capacité maximale des villes.

On constate donc que la capacité globale du réseau ne dépend pas uniquement des routes, mais aussi des capacités des villes intermédiaires.
Cela montre que l'introduction de contraintes plus réalistes réduit la performance du réseau et permet de mieux identifier les points critiques qui limitent la circulation.

"""
                    ),
                ]
            ),
            "Question 4": mo.vstack(
    [
        mo.md("""
# Question 4

Dans cette question, on cherche à comprendre l'influence de la capacité d'une ville sur le flot maximal du réseau.
On fait varier la capacité de la ville `d`, tout en gardant les autres paramètres constants.
Pour chaque valeur de capacité, on recalcule le flot maximal afin d'observer comment le réseau réagit à cette modification.
L'objectif est d'identifier si cette ville constitue un point limitant du réseau et de voir à partir de quel moment augmenter sa capacité n'a plus d'effet.


Le curseur permet de modifier la capacité de `d`.
"""),
        capacite_d,
        mo.md(
            f"Pour une capacité de **d = {capacite_d.value}**, le flot maximal vaut : **{flot_interactif_q4}**"
        ),

        mo.md("## Analyse des résultats"),

        mo.hstack([
            fig_q4,
            mo.md(tableau_q4)
        ]),

        mo.md("""
## Interprétation


On observe que le flot maximal augmente progressivement lorsque la capacité de la ville `d` augmente, passant de 12 à 16.
Cela montre que, pour les petites capacités, la ville `d` constitue un goulot d'étranglement : elle limite directement le flux dans le réseau.

Cependant, à partir d'une certaine valeur (ici 5), le flot maximal se stabilise à 16.  
Cela signifie qu'augmenter davantage la capacité de la ville `d` n'a plus d'impact.
On en déduit que d'autres contraintes dans le réseau deviennent alors limitantes (routes ou autres villes).
Ainsi, la ville `d` influence le flot maximal uniquement jusqu'à un certain seuil, après quoi elle n'est plus le facteur limitant du réseau.
"""),
    ]
),
        }
    )

    dashboard
    return


if __name__ == "__main__":
    app.run()
    