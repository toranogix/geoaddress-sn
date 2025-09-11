import folium
import geopandas as gpd
from typing import List
from utils import logger
from pathlib import Path


class MapGenerator:
    """Class to generate the interactive map"""
    
    def __init__(self, routes_quartiers: gpd.GeoDataFrame, quartiers_gdf: gpd.GeoDataFrame):
        self.routes_quartiers = routes_quartiers
        self.quartiers_gdf = quartiers_gdf
        self.map_center = self.calculate_map_center()
        self.m = None
        
    def calculate_map_center(self) -> List[float]:
        """Calculate the center of the map"""
        if len(self.quartiers_gdf) > 0:
            center_geom = self.quartiers_gdf.iloc[0].geometry
            if hasattr(center_geom, 'centroid'):
                return [center_geom.centroid.y, center_geom.centroid.x]
        return [14.6928, -17.4467] # default coordinates
    
    def simplify_geometry(self, geom, tolerance: float = 0.0001):
        """Simplify the geometry for better performance"""
        try:
            return geom.simplify(tolerance)
        except:
            return geom
    
    def get_optimized_routes(self, max_routes: int = 1000) -> gpd.GeoDataFrame:
        """Return an optimized sample of routes"""
        if len(self.routes_quartiers) > max_routes:
            logger.info(f"Trop de routes ({len(self.routes_quartiers)}), affichage limité à {max_routes}")
            return self.routes_quartiers.sample(n=max_routes, random_state=42)
        return self.routes_quartiers
    
    def create_map(self) -> None:
        """Create the base map"""
        self.m = folium.Map(
            location=self.map_center, 
            zoom_start=10, 
            tiles='OpenStreetMap'
        )
    
    def add_quartier_boundaries(self) -> None:     
        """Add the boundaries of the quartiers"""
        for _, row in self.quartiers_gdf.iterrows():
            if row.geometry is not None:
                simplified_geom = self.simplify_geometry(row.geometry, tolerance=0.0005)
                folium.GeoJson(
                    simplified_geom,
                    style_function=lambda x: {"color": "red", "weight": 2, "fillOpacity": 0.05},
                    tooltip=f"Quartier: {row['quartier_nom']}"
                ).add_to(self.m)
    
    def add_routes(self, max_routes: int = 1000) -> None:
        """Add the routes to the map"""
        routes_to_display = self.get_optimized_routes(max_routes)
        routes_group = folium.FeatureGroup(name="Routes nommées")
        
        def optimized_style_function(feature):
            return {
                "color": "#1f77b4",
                "weight": 1.5,
                "opacity": 0.7,
                "fillOpacity": 0
            }
        
        batch_size = 10
        for i in range(0, len(routes_to_display), batch_size):
            batch = routes_to_display.iloc[i:i+batch_size]
            
            for _, row in batch.iterrows():
                if row.geometry is not None:
                    simplified_route = self.simplify_geometry(row.geometry, tolerance=0.0001)
                    tooltip_text = f"Route: {row['nom_attribue']}"
                    
                    folium.GeoJson(
                        simplified_route,
                        style_function=optimized_style_function,
                        tooltip=tooltip_text,
                        popup=folium.Popup(tooltip_text, max_width=200)
                    ).add_to(routes_group)
        
        routes_group.add_to(self.m)
        logger.info(f"{len(routes_to_display)} routes ajoutées à la carte")
    
    def add_controls(self) -> None:
        """Add the controls of the map"""
        folium.LayerControl().add_to(self.m)
    
    def generate_map(self, output_file: str = "html/carte_test.html", max_routes: int = 1000) -> None:

        """Generate the complete interactive map"""

        # create html directory if it doesn't exist
        Path(output_file).parent.mkdir(parents=True, exist_ok=True)
        self.create_map()
        self.add_quartier_boundaries()
        self.add_routes(max_routes)
        self.add_controls()
        
        self.m.save(output_file)
        logger.info(f"Carte générée : {output_file}")
    
    def get_map(self) -> folium.Map:
        return self.m
