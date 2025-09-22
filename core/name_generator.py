import pandas as pd
from pathlib import Path
from utils.utils import logger
import random
from config.urban_typology import get_urban_typology, get_typology_config
from config.name_categories import get_name_categories


class NameGenerator:
    """Class to generate and manage street names based on urban typology"""

    def __init__(self, n_names: int = 100, quarter_name: str = None, typology: str = None):
        self.n_names = n_names
        self.quarter_name = quarter_name
        self.typology = typology or (get_urban_typology(quarter_name) if quarter_name else "residentiel_populaire")
        self.typology_config = get_typology_config(self.typology)
        self.name_categories = get_name_categories(self.typology)
        self.noms = self._generate_typology_specific_names()

    def _generate_typology_specific_names(self) -> list:
        """Generate names specific to the urban typology"""
        noms = set()
        
        # Get available route types for this typology
        route_types = self.name_categories["voies"]
        
        # Get naming elements
        personnalites = self.name_categories["personnalites"]
        concepts = self.name_categories["concepts"]
        lieux = self.name_categories.get("lieux_officiels", 
                                       self.name_categories.get("lieux_traditionnels",
                                       self.name_categories.get("lieux_prestigieux",
                                       self.name_categories.get("lieux_communautaires",
                                       self.name_categories.get("lieux_commerciaux",
                                       self.name_categories.get("lieux_industriels",
                                       self.name_categories.get("lieux_touristiques", [])))))))
        
        # Combine all naming elements
        all_elements = personnalites + concepts + lieux
        
        # Generate names
        while len(noms) < self.n_names:
            voie = random.choice(route_types)
            element = random.choice(all_elements)
            nom = f"{voie} {element}"
            noms.add(nom)
        
        return list(noms)

    def save_names_to_csv(self, filename: str = "data/names.csv") -> None:
        """Save names to CSV with typology information"""
        # Create data directory if it doesn't exist
        Path(filename).parent.mkdir(parents=True, exist_ok=True)
        
        # Create DataFrame with typology information
        df = pd.DataFrame({
            "name": self.noms,
            "typology": [self.typology] * len(self.noms),
            "quarter": [self.quarter_name] * len(self.noms) if self.quarter_name else [None] * len(self.noms)
        })
        
        df.to_csv(filename, index=False, encoding="utf-8")
        logger.info(f"Fichier '{filename}' généré avec succès pour la typologie '{self.typology}'")

    def get_names_list(self) -> list:
        """Return the list of names"""
        return self.noms.copy()
    
    def get_typology_info(self) -> dict:
        """Return information about the current typology"""
        return {
            "typology": self.typology,
            "quarter": self.quarter_name,
            "config": self.typology_config,
            "naming_style": self.typology_config.get("naming_style", "communautaire")
        }
