import osmnx as ox
import geopandas as gpd
import pandas as pd
import random
from utils.utils import logger
from config.urban_typology import get_urban_typology, get_typology_config
from config.name_categories import get_name_categories


class RouteNamer:
    """Classe pour gérer l'attribution de noms aux routes en fonction de la typologie urbaine"""
    
    def __init__(self, ville: str, filter_quartier: str):
        self.ville = ville
        self.filter_quartier = filter_quartier
        self.typology = get_urban_typology(filter_quartier)
        self.typology_config = get_typology_config(self.typology)
        self.name_categories = get_name_categories(self.typology)
        self.names_list = []
        self.routes_gdf = None
        self.quartiers_gdf = None
        self.routes_quartiers = None
        
        logger.info(f"Typologie urbaine détectée: {self.typology} pour le quartier {filter_quartier}")
        
    def load_names(self, names_file: str = "data/output/names.csv") -> None:
        """Chargement de la liste des noms depuis le fichier CSV"""
        try:
            names_df = pd.read_csv(names_file)
            self.names_list = names_df['name'].dropna().unique().tolist()
            logger.info(f"{len(self.names_list)} noms chargés depuis {names_file}")
        except FileNotFoundError:
            logger.error(f"Fichier {names_file} non trouvé")
            raise
    
    def download_routes(self) -> None:
        """Téléchargement des routes du quartier spécifié"""
        logger.info(f"Téléchargement des routes pour le quartier {self.filter_quartier}...")
        try:
            G = ox.graph_from_place(f"{self.filter_quartier}, {self.ville}", network_type="drive")
            self.routes_gdf = ox.graph_to_gdfs(G, nodes=False, edges=True)
            self.routes_gdf = self.routes_gdf.to_crs(epsg=4326)
            self.routes_gdf.to_file("data/output/routes_quartier_test.geojson", driver="GeoJSON")
            logger.info(f"{len(self.routes_gdf)} routes téléchargées")
        except Exception as e:
            logger.error(f"Erreur lors du téléchargement des routes: {e}")
            raise
    

    def load_quartiers_data(self, filter_quartier: str) -> gpd.GeoDataFrame:
        """Récupération des données des quartiers depuis le fichier"""

        logger.info(f"Traitement du quartier {filter_quartier}...")
        try:
            self.quartiers_gdf = gpd.read_file("data/data_dkr/Quartier.shp")
            filter_quartier = filter_quartier.strip().lower()
            self.quartiers_gdf["CCRCA"] = self.quartiers_gdf["CCRCA"].str.strip().str.lower()  # delete spaces and uppercase
            self.quartiers_gdf = self.quartiers_gdf[self.quartiers_gdf["CCRCA"] == filter_quartier]
            self.quartiers_gdf = self.quartiers_gdf.to_crs(epsg=4326)
            self.quartiers_gdf.to_file("data/output/quartier_test.geojson", driver="GeoJSON", index=False)
            logger.info(f"Traitement des données du quartier {filter_quartier} OK.")

        except Exception as e:
            logger.error(f"Erreur lors du téléchargement des quartiers: {e}")
            raise
    
    def associate_routes_to_quartiers(self) -> None:
        """Correspondance des routes aux quartiers"""
        if self.routes_gdf is None or self.quartiers_gdf is None:
            raise ValueError("Routes et quartiers doivent être traités d'abord")
        
        self.routes_quartiers = gpd.sjoin(
            self.routes_gdf, 
            self.quartiers_gdf, 
            how="left", 
            predicate="intersects"
        )
        self.routes_quartiers["nom_attribue"] = None
        logger.info(f"{len(self.routes_quartiers)} routes associées aux quartiers")
    
    def assign_names_to_routes(self) -> None:
        """Attribution de noms aux routes en fonction de la typologie urbaine. Si la route a un nom, il n'est pas attribué un nouveau nom """
        
        if self.routes_quartiers is None:
            raise ValueError("Routes et quartiers doivent être traités d'abord")
        
        # Génération des noms spécifiques à la typologie si non déjà chargés
        if not self.names_list:
            self._generate_typology_specific_names()
        
        noms_disponibles = self.names_list.copy()
        random.shuffle(noms_disponibles)
        
        routes_with_original_names = 0
        routes_with_new_names = 0
        
        for i, (idx, row) in enumerate(self.routes_quartiers.iterrows()):
            # Vérification si la route a déjà un nom 
            if pd.notna(row["name"]) and row["name"] is not None and str(row["name"]).strip() != "":
                nom = row["name"]
                routes_with_original_names += 1
            else:
                # SInon, attribution d'un nom selon la typologie urbaine
                nom = self._get_appropriate_name_for_route(row, noms_disponibles, i)
                routes_with_new_names += 1
            self.routes_quartiers.loc[idx, "nom_attribue"] = nom
        
        logger.info(f"{len(self.routes_quartiers)} routes ont reçu un nom")
        logger.info(f"- {routes_with_original_names} routes ont conservé leur nom")
        logger.info(f"- {routes_with_new_names} routes ont reçu un nouveau nom")
        logger.info(f"Typologie utilisée: {self.typology} ({self.typology_config['name']})")
    
    def _generate_typology_specific_names(self) -> None:
        """Génération des noms spécifiques en fonction de la typologie urbaine"""
        noms = set()
        
        # Récupération des types de routes  
        route_types = self.name_categories["voies"]
        
        # Récupération des éléments de nommage
        personnalites = self.name_categories["personnalites"]
        concepts = self.name_categories["concepts"]
        lieux = self.name_categories.get("lieux_officiels", 
                                       self.name_categories.get("lieux_traditionnels",
                                       self.name_categories.get("lieux_prestigieux",
                                       self.name_categories.get("lieux_communautaires",
                                       self.name_categories.get("lieux_commerciaux",
                                       self.name_categories.get("lieux_industriels",
                                       self.name_categories.get("lieux_touristiques", [])))))))
        
        # Combinaison de tous les éléments de nommage
        all_elements = personnalites + concepts + lieux
        
        # Génération des noms
        while len(noms) < 200:  
            voie = random.choice(route_types)
            element = random.choice(all_elements)
            nom = f"{voie} {element}"
            noms.add(nom)
        
        self.names_list = list(noms)
        logger.info(f"Généré {len(self.names_list)} noms spécifiques à la typologie {self.typology}")
    
    def _get_appropriate_name_for_route(self, route_row, noms_disponibles, index) -> str:
        """Récupération d'un nom approprié pour une route en fonction de ses caractéristiques et de la typologie urbaine"""
 
        return noms_disponibles[index % len(noms_disponibles)]
    
    def run_pipeline(self) -> None:
        self.download_routes()
        self.load_quartiers_data(self.filter_quartier)
        self.associate_routes_to_quartiers()
        self.assign_names_to_routes()
    
    def get_routes_data(self) -> gpd.GeoDataFrame:
        """Retourne les données des routes avec les noms attribués"""
        return self.routes_quartiers
    
    def get_quartiers_data(self) -> gpd.GeoDataFrame:
        """Retourne les données des quartiers"""
        return self.quartiers_gdf
