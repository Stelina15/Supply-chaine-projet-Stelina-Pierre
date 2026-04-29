"""Description.

Module de modélisation d'un réseau routier.
"""

from typing_extensions import Self
from pydantic import BaseModel, PositiveInt, model_validator


class Route(BaseModel):
    """Représente une route orientée avec une capacité."""

    depart: str
    arrivee: str
    capacite: PositiveInt

    @model_validator(mode="after")
    def verifie_extremites(self) -> Self:
        """Vérifie que la route ne relie pas une ville à elle-même."""
        if self.depart == self.arrivee:
            msg = "Une route ne peut pas relier une ville à elle-même"
            raise ValueError(msg)
        return self


class Reseau(BaseModel):
    """Représente un réseau routier orienté."""

    villes: list[str]
    routes: list[Route]
    source: str
    puits: str

    @model_validator(mode="after")
    def verifie_villes_uniques(self) -> Self:
        """Vérifie que les villes sont distinctes."""
        if len(set(self.villes)) != len(self.villes):
            msg = "Les villes doivent être distinctes"
            raise ValueError(msg)
        return self

    @model_validator(mode="after")
    def verifie_source_puits(self) -> Self:
        """Vérifie que la source et le puits sont valides."""
        if self.source not in self.villes:
            msg = "La source doit être une ville du réseau"
            raise ValueError(msg)
        if self.puits not in self.villes:
            msg = "Le puits doit être une ville du réseau"
            raise ValueError(msg)
        if self.source == self.puits:
            msg = "La source et le puits doivent être différents"
            raise ValueError(msg)
        return self

    @model_validator(mode="after")
    def verifie_routes(self) -> Self:
        """Vérifie la cohérence des routes."""
        routes_vues = set()

        for route in self.routes:
            if route.depart not in self.villes:
                msg = f"Ville inconnue : {route.depart}"
                raise ValueError(msg)
            if route.arrivee not in self.villes:
                msg = f"Ville inconnue : {route.arrivee}"
                raise ValueError(msg)

            cle = (route.depart, route.arrivee)
            if cle in routes_vues:
                msg = "Deux routes ne peuvent pas avoir le même départ et la même arrivée"
                raise ValueError(msg)
            routes_vues.add(cle)

        return self