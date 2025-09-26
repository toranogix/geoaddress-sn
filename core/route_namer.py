import osmnx as ox
import geopandas as gpd
import pandas as pd
import random
from utils.utils import logger


class RouteNamer:
    """Classe pour gérer la gestion de l'attribution de noms aux rues"""
    
    def __init__(self, ville: str, filter_quartier: str):
        self.ville = ville
        self.filter_quartier = filter_quartier
        self.names_list = []
        self.routes_gdf = None
        self.quartiers_gdf = None
        self.routes_quartiers = None
        
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
        """Traitement des données du quartier"""
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
        """Attribution de noms aux routes. Si la route a un nom, il n'est pas attribué un nouveau nom """
        
        if self.routes_quartiers is None:
            raise ValueError("Routes et quartiers doivent être traités d'abord")
        
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
                # sinon attribue un nouveau nom
                nom = noms_disponibles[i % len(noms_disponibles)]
                routes_with_new_names += 1
            self.routes_quartiers.loc[idx, "nom_attribue"] = nom
        
        logger.info(f"{len(self.routes_quartiers)} routes ont reçu un nom")
        logger.info(f"- {routes_with_original_names} routes ont conservé leur nom")
        logger.info(f"- {routes_with_new_names} routes ont reçu un nouveau nom")
    
    def run_pipeline(self) -> None:
        """Exécution du pipeline complet"""
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
