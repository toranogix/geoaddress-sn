from core.name_generator import NameGenerator
from core.map_generator import MapGenerator
from core.route_namer import RouteNamer
from utils.utils import logger
import datetime

def main():
    """Main function with urban typology support"""
    ville = "Dakar, Senegal"
    filter_quartier = "Yoff"
    
    try:
        # 1. Generate typology-specific names
        start_time = datetime.datetime.now()
        logger.info(f"{start_time} - Début du processus de nommage des routes avec typologie urbaine")
        
        # Generate names specific to the quarter's typology
        name_generator = NameGenerator(n_names=100, quarter_name=filter_quartier)
        name_generator.save_names_to_csv("data/output/names.csv")
        
        # Log typology information
        typology_info = name_generator.get_typology_info()
        logger.info(f"Typologie détectée: {typology_info['typology']} - {typology_info['config']['name']}")
        logger.info(f"Style de nommage: {typology_info['naming_style']}")
        
        # 2. Create and run the pipeline
        route_namer = RouteNamer(ville, filter_quartier)
        route_namer.load_names("data/output/names.csv")
        route_namer.run_pipeline()
        
        # 3. Generate the map
        map_generator = MapGenerator(
            route_namer.get_routes_data(), 
            route_namer.get_quartiers_data()
        )
        map_generator.generate_map()
        
        # 4. Summary
        logger.info(f"Test effectué sur le quartier {filter_quartier}")
        logger.info(f"Typologie urbaine: {route_namer.typology} ({route_namer.typology_config['name']})")
        logger.info(f"Routes affichées: {len(route_namer.get_routes_data())} totales")
        logger.info("Processus terminé avec succès !")

        end_time = datetime.datetime.now()
        logger.info(f"{end_time} - Processus terminé en {end_time - start_time}")
        
    except Exception as e:
        logger.error(f"Erreur lors de l'exécution: {e}")
        raise

if __name__ == "__main__":
    main()
