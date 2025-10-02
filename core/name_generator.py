import pandas as pd
from pathlib import Path
from utils.utils import logger
import random
from config.config import TYPE_VOIES, KEYWORDS


class NameGenerator:
    """Classe pour générer et gérer les noms des rues"""
    # TODO: Améliorer la génération des noms

    def __init__(self, n_names: int = 100):
        noms = set()
        max_possible = len(TYPE_VOIES) * len(KEYWORDS)
        
        # Limiter le nombre de noms demandés au maximum possible
        n_names = min(n_names, max_possible)
        
        # Génération de noms uniques
        while len(noms) < n_names:
            voie = random.choice(TYPE_VOIES)
            mot = random.choice(KEYWORDS)
            nom = f"{voie} {mot}"
            noms.add(nom)
        self.noms = list(noms)
        
        logger.info(f"{len(self.noms)} noms uniques générés (maximum possible: {max_possible})")

    def save_names_to_csv(self, filename: str = "data/output/names.csv") -> None:

        Path(filename).parent.mkdir(parents=True, exist_ok=True)
        df = pd.DataFrame({"name": self.noms})
        df.to_csv(filename, index=False, encoding="utf-8")
        logger.info(f"Fichier '{filename}' généré avec succès")

    def get_names_list(self) -> list:
        """Retourne la liste des noms"""
        return self.noms.copy()
