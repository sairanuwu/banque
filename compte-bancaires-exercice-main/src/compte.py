import uuid
from abc import ABC


class Compte(ABC):
    """
        Abstract class Compte
    """

    def __init__(self, nomProprietaire, **kwargs):
        self.nom_proprietaire = nomProprietaire
        self.numero_compte = kwargs.get("numero_compte")
        self.solde = kwargs.get("solde")

    def retrait(self, montant):
        self.solde -= montant

    def versement(self, montant):
        if montant <= 0:
            raise Exception
        self.solde += montant

    def afficherSolde(self):  # pragma: no cover
        pass

    def __repr__(self):
        return f"CompteCourant - Solde : {self.solde}"


class CompteCourant(Compte):
    def __init__(self, nomProprietaire, **kwargs):
        super().__init__(nomProprietaire, solde=0, numero_compte=kwargs.get("numero_compte"))
        self.autorisation_decouvert = kwargs.get("autorisation_decouvert", True)
        self.pourcentage_agios = kwargs.get("agios")

    def appliquer_agios(self, montant):
        if self.solde < 0:
            self.solde -= montant * self.pourcentage_agios

    def retrait(self, montant):
        if montant <= 0 or not self.autorisation_decouvert:
            raise Exception
        super().retrait(montant)
        self.appliquer_agios(montant)


class CompteEpargne(Compte):
    def __init__(self, nomProprietaire, **kwargs):
        super().__init__(nomProprietaire, solde=0, numero_compte=kwargs.get("numero_compte"))
        self.pourcentage_interets = kwargs.get("pourcentage_interets")

    def appliquer_interet(self):
        if self.montant > 0:
            self.solde = self.montant * (1 + (10 / 100))
        return self.solde


