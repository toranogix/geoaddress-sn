import pandas as pd
import logging
import random

logger = logging.getLogger(__name__)

class NameGenerator:
    """Class to generate and manage street names"""

    def __init__(self, n_names: int = 100):

        types_voies = [
            "Rue", "Avenue", "Boulevard", "Chemin", "Allée", "Route"
        ]

        # Keywords
        keywords = [
            "Liberté", "Soleil", "Palmiers", "Baobabs", "Plage", "Almadies", "Yoff",
            "Océan", "Lions", "Horizon", "Manguiers", "Colibris", "Ouakam", "Pirogues",
            "Gorée", "Phare", "Écoles", "Renaissance", "Marché", "Hibiscus",
            "Sénégal", "Dakar", "Ngor", "Corniche", "Sable", "Médina", "Soumbédioune",
            "Kermel", "Plateau", "Ngor Virage", "Pikine", "Guédiawaye", "Caméléons",
            "Casuarinas", "Iles", "Cocotiers", "Niap", "Carapaces", "Diodio",
            "Pastèques", "Mango", "Tam-tam", "Safran", "Fleur d'Or", "Étoiles",
            "Vent", "Lagune", "Poissons", "Cauri", "Perles", "Mousso", "Dunes",
            "Campement", "Aurore", "Colline", "Parasol", "Vagues", "Marine",
            "Samba", "Sabliers", "Navétanes", "Baie", "Espoir", "Union", "Cap",
            "Teranga", "Paix", "Fadj", "Jigeen", "Ndiaye", "Fall", "Diop",
            "Diallo", "Sy", "Sarr", "Gueye", "Ba", "Mbaye", "Ndao", "Seck",
            "Wade", "Ka", "Badiane", "Faye", "Diagne", "Mbengue", "Lô", "Cissé",
            "Thiam", "Ndour", "Gomis", "Mané", "Sagna", "Sadio", "Sonko", "Bop",
            "Coumba", "Keur", "Samba Laobé", "Mame Diarra"
        ]

        noms = set()
        # Generate n_names unique names
        while len(noms) < n_names:
            voie = random.choice(types_voies)
            mot = random.choice(keywords)
            nom = f"{voie} {mot}"
            noms.add(nom)
        self.noms = list(noms)

    def save_names_to_csv(self, filename: str = "data/names.csv") -> None:
        df = pd.DataFrame({"name": self.noms})
        df.to_csv(filename, index=False, encoding="utf-8")
        logger.info(f"Fichier '{filename}' généré avec succès")

    def get_names_list(self) -> list:
        """Return the list of names"""
        return self.noms.copy()
