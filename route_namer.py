import osmnx as ox
import geopandas as gpd
import pandas as pd
import random
import logging
from typing import List

logger = logging.getLogger(__name__)

class RouteNamer:
    """Manage the assignment of names to routes"""
    
    def __init__(self, ville: str, quartier_test: str = "Yoff"):
        self.ville = ville
        self.quartier_test = quartier_test
        self.names_list = []
        self.routes_gdf = None
        self.quartiers_gdf = None
        self.routes_quartiers = None
        
    def load_names(self, names_file: str = "data/names.csv") -> None:
        """Load the list of names from the CSV file"""
        try:
            names_df = pd.read_csv(names_file)
            self.names_list = names_df['name'].dropna().unique().tolist()
            logger.info(f"{len(self.names_list)} noms chargés depuis {names_file}")
        except FileNotFoundError:
            logger.error(f"Fichier {names_file} non trouvé")
            raise
    
    def download_routes(self) -> None:
        """Download the routes of the specified quarter"""
        logger.info(f"Téléchargement des routes pour le quartier {self.quartier_test}...")
        try:
            G = ox.graph_from_place(f"{self.quartier_test}, {self.ville}", network_type="drive")
            self.routes_gdf = ox.graph_to_gdfs(G, nodes=False, edges=True)
            self.routes_gdf = self.routes_gdf.to_crs(epsg=4326)
            self.routes_gdf.to_file("data/routes_quartier_test.geojson", driver="GeoJSON")
            logger.info(f"{len(self.routes_gdf)} routes téléchargées")
        except Exception as e:
            logger.error(f"Erreur lors du téléchargement des routes: {e}")
            raise
    
    def download_quartiers(self) -> None:
        """Download the data"""
        logger.info(f"Téléchargement du quartier {self.quartier_test}...")
        try:
            self.quartiers_gdf = ox.features_from_place(
                f"{self.quartier_test}, {self.ville}",
                tags={"boundary": "administrative", "admin_level": "10"}
            )
            self.quartiers_gdf = self.quartiers_gdf[
                self.quartiers_gdf.geom_type.isin(["Polygon", "MultiPolygon"])
            ]
            self.quartiers_gdf["quartier_nom"] = self.quartiers_gdf.get("name")
            self.quartiers_gdf = self.quartiers_gdf.to_crs(epsg=4326)
            self.quartiers_gdf.to_file("data/quartier_test.geojson", driver="GeoJSON")
            logger.info(f"{len(self.quartiers_gdf)} quartiers téléchargés")
        except Exception as e:
            logger.error(f"Erreur lors du téléchargement des quartiers: {e}")
            raise
    
    def associate_routes_to_quartiers(self) -> None:
        """Associate the routes """
        if self.routes_gdf is None or self.quartiers_gdf is None:
            raise ValueError("Routes et quartiers doivent être téléchargés d'abord")
        
        self.routes_quartiers = gpd.sjoin(
            self.routes_gdf, 
            self.quartiers_gdf, 
            how="left", 
            predicate="intersects"
        )
        self.routes_quartiers["nom_attribue"] = None
        logger.info(f"{len(self.routes_quartiers)} routes associées aux quartiers")
    
    def assign_names_to_routes(self) -> None:
        """Assign names to the roads"""
        if self.routes_quartiers is None:
            raise ValueError("Routes et quartiers doivent être associés d'abord")
        
        noms_disponibles = self.names_list.copy()
        random.shuffle(noms_disponibles)
        
        for i, (idx, row) in enumerate(self.routes_quartiers.iterrows()):
            nom = noms_disponibles[i % len(noms_disponibles)]
            self.routes_quartiers.loc[idx, "nom_attribue"] = nom
        
        logger.info(f"{len(self.routes_quartiers)} routes ont reçu un nom")
    
    def run_pipeline(self) -> None:
        """Run the complete pipeline"""
        self.download_routes()
        self.download_quartiers()
        self.associate_routes_to_quartiers()
        self.assign_names_to_routes()
    
    def get_routes_data(self) -> gpd.GeoDataFrame:
        """Return the data of the roads with assigned names"""
        return self.routes_quartiers
    
    def get_quartiers_data(self) -> gpd.GeoDataFrame:
        """Return the data """
        return self.quartiers_gdf
