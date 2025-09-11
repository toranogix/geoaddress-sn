
from name_generator import NameGenerator
from route_namer import RouteNamer
from map_generator import MapGenerator
from utils import logger

def main():
    """Main function"""
    ville = "Dakar, Senegal"
    quartier_test = "Yoff"
    
    try:
        # 1. Generate names
        logger.info("Début du processus de nommage des routes")
        name_generator = NameGenerator()
        name_generator.save_names_to_csv()
        
        # 2. Create and run the pipeline
        route_namer = RouteNamer(ville, quartier_test)
        route_namer.load_names()
        route_namer.run_pipeline()
        
        # 3. Generate the map
        map_generator = MapGenerator(
            route_namer.get_routes_data(), 
            route_namer.get_quartiers_data()
        )
        map_generator.generate_map()
        
        # 4. Summary
        logger.info(f"Test effectué sur le quartier {quartier_test}")
        logger.info(f"Routes affichées: {len(route_namer.get_routes_data())} totales")
        logger.info("Processus terminé avec succès !")
        
    except Exception as e:
        logger.error(f"Erreur lors de l'exécution: {e}")
        raise

if __name__ == "__main__":
    main()
