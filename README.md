# 🚗 Projet réseau routier — Flot maximal

## 📌 Présentation du projet

Ce projet étudie un problème de circulation dans un réseau routier.

Le réseau est composé de villes reliées par des routes. Chaque route possède une capacité, c’est-à-dire un débit maximal de véhicules pouvant circuler dessus.

L’objectif principal est de calculer le **flot maximal** entre une ville de départ `E` et une ville d’arrivée `S`.

---

## 🎯 Objectifs

Le projet répond à plusieurs questions :

- déterminer le débit maximal entre `E` et `S`
- modéliser le réseau sous forme de graphe orienté
- ajouter des capacités sur les villes intermédiaires
- analyser l’influence de la capacité d’une ville sur le flot total
- visualiser les résultats avec un dashboard `marimo`

---

## 🧠 Méthode utilisée

Le réseau est représenté sous forme de **graphe orienté** avec la bibliothèque `networkx`.

- les sommets représentent les villes  
- les arêtes représentent les routes  
- les capacités représentent le flux maximal autorisé  

Dans un premier temps, le flot maximal est calculé uniquement avec les capacités des routes.

Ensuite, on ajoute des capacités sur les villes. Pour cela, chaque ville intermédiaire est transformée en deux sommets :

- `ville_entree`
- `ville_sortie`

Ces deux sommets sont reliés par une arête correspondant à la capacité maximale de la ville.

Cette transformation permet d’utiliser les algorithmes classiques de flot maximal, qui fonctionnent uniquement sur les arêtes.

Les données du réseau sont désormais stockées dans un fichier reseau.json.

Cette approche permet de séparer les données du code source. Le programme charge automatiquement le réseau depuis ce fichier grâce au module json_loader.py.

Il devient ainsi possible de modifier la structure du réseau, les routes ou les capacités sans changer le code Python.

---

## 📊 Résultats principaux

- Flot maximal sans capacité sur les villes : **18**
- Flot maximal avec capacités sur les villes : **16**

👉 L’ajout de contraintes réduit la capacité globale du réseau.

---

## 📂 Structure du projet
```text

SUPPLY-CHAIN-PROJET-MAIN/

├── src/
│   ├── notebooks/
│   │   └── exploration.ipynb
│   │
│   └── reseau_routier/
│       ├── __init__.py
│       ├── cli.py
│       ├── data.py
│       ├── exemple.py
│       ├── flot.py
│       ├── json_loader.py
│       ├── modeles.py
│       └── visugraphe.py
│
├── tests/
│   ├── test_data.py
│   ├── test_exemples.py
│   ├── test_flot.py
│   └── test_modeles.py
│
├── reseau.json
├── visualisation.py
├── pyproject.toml
├── uv.lock
├── .gitignore
└── README.md  
```

---

## 🛠️ Outils utilisés

- Python  
- networkx  
- matplotlib  
- marimo  
- pytest  
- uv 
- typer
- ruff
- mypy
 

---

## ⚙️ Installation

Le projet utilise `uv` pour gérer l’environnement Python.

Pour installer toutes les dépendances :

uv sync

Cette commande crée l’environnement virtuel et installe toutes les librairies nécessaires.

Si on devait créer un projet depuis zéro :

uv init

---

## ▶️ Lancer le projet

### Lancer le programme principal

Afficher les résultats principaux:

uv run python -m reseau_routier.cli tout

Afficher les questions 1 et 3 :
uv run python -m reseau_routier.cli exemple

Analyser la ville d :
uv run python -m reseau_routier.cli analyse-ville d
uv run python -m reseau_routier.cli meilleure-capacite --ville d

---
#### Lancer le dashboard interactif

uv run marimo run visualisation.py

Une URL apparaît dans le terminal (ex: http://localhost:2718)

Ouvrir ce lien dans le navigateur.

Le dashboard permet de :

- visualiser les graphes
- voir les résultats des différentes questions
- modifier interactivement la capacité d’une ville
- sélectionner la ville étudiée
- analyser l’évolution du flot maximal

---

## 🧪 Tests

Pour lancer les tests :

uv run pytest

Les tests vérifient :

- la construction du réseau
- les calculs de flot
- la transformation du graphe
- la validité des résultats

---
## Qualité du code 
Pour vérifier la qualité du code avec ruff :
uv run ruff check .

Pour formater automatiquement le code :
uv run ruff format

---

##  Type checking
Pour vérifier les types avec mypy :
uv run mypy src/reseau_routier

---

### 📌 Organisation du code

data.py  
→ définit les structures du réseau (routes, villes)

exemple.py  
→ contient les données du sujet

json_loader.py
→ charge les données du réseau depuis un fichier JSON

flot.py  
→ calcule le flot maximal

modeles.py  
→ transforme le graphe (capacités sur les villes)

visugraphe.py  
→ affiche les graphes

visualisation.py  
→ dashboard interactif marimo

---

## 💡 Conclusion

Le projet montre que le flot maximal dépend à la fois des routes et des villes.

Certaines villes peuvent devenir des **goulots d’étranglement** et limiter le flux global.

L’analyse permet d’identifier les points critiques du réseau et de mieux comprendre son fonctionnement.

Les données du réseau étant désormais chargées depuis un fichier JSON, le projet peut être adapté à d’autres réseaux routiers sans modifier le code source.
