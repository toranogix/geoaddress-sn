import pandas as pd
from pathlib import Path
from utils.utils import logger
import random
from config.urban_typology import get_urban_typology, get_typology_config
from config.name_categories import get_name_categories


class NameGenerator:
    """ Classe pour générer les noms spécifiques à la typologie
    """

    def __init__(self, n_names: int = 100, quarter_name: str = None, typology: str = None):
        self.n_names = n_names
        self.quarter_name = quarter_name
        self.typology = typology or (get_urban_typology(quarter_name) if quarter_name else "residentiel_populaire")
        self.typology_config = get_typology_config(self.typology)
        self.name_categories = get_name_categories(self.typology)
        self.noms = self._generate_typology_specific_names()

    def _generate_typology_specific_names(self) -> list:
        """Générer les noms spécifiques à la typologie

        Returns:
            list: Liste des noms
        """
        noms = set()
        
        # Récupérer les types de voies pour chaque typologie
        route_types = self.name_categories["voies"]
        
        # Récupérer les éléments de nommage
        personnalites = self.name_categories["personnalites"]
        concepts = self.name_categories["concepts"]
        lieux = self.name_categories.get("lieux_officiels", 
                                       self.name_categories.get("lieux_traditionnels",
                                       self.name_categories.get("lieux_prestigieux",
                                       self.name_categories.get("lieux_communautaires",
                                       self.name_categories.get("lieux_commerciaux",
                                       self.name_categories.get("lieux_industriels",
                                       self.name_categories.get("lieux_touristiques", [])))))))
        
        # Combiner tous les éléments de nommage
        all_elements = personnalites + concepts + lieux
        
        # Génération des noms
        while len(noms) < self.n_names:
            voie = random.choice(route_types)
            element = random.choice(all_elements)
            nom = f"{voie} {element}"
            noms.add(nom)
        
        return list(noms)

    def save_names_to_csv(self, filename: str = "data/names.csv") -> None:
        """Enregistrer les noms dans un fichier CSV avec les informations de la typologie

        Args:
            filename (str, optional): Nom du fichier. ".
        """

        Path(filename).parent.mkdir(parents=True, exist_ok=True)
        
        # Création d'un df avec les informations de la typologie
        df = pd.DataFrame({
            "name": self.noms,
            "typology": [self.typology] * len(self.noms),
            "quarter": [self.quarter_name] * len(self.noms) if self.quarter_name else [None] * len(self.noms)
        })
        
        df.to_csv(filename, index=False, encoding="utf-8")
        logger.info(f"Fichier '{filename}' généré avec succès pour la typologie '{self.typology}'")

    def get_names_list(self) -> list:
        return self.noms.copy()
    
    def get_typology_info(self) -> dict:
        """Retourner les informations sur la typologie

        Returns:
            dict: Informations sur la typologie
        """
        return {
            "typology": self.typology,
            "quarter": self.quarter_name,
            "config": self.typology_config,
            "naming_style": self.typology_config.get("naming_style", "communautaire")
        }
