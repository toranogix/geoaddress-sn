from core.name_generator import NameGenerator
from core.map_generator import MapGenerator
from core.route_namer import RouteNamer
from utils.utils import logger
import datetime



def main():
    """Fonction principale
    """
    ville = "Dakar, Senegal"
    filter_quartier = "Yoff"
    
    try:
        # 1. Création des noms
        start_time = datetime.datetime.now()
        logger.info(f"{start_time} - Début du processus de nommage des routes")
        name_generator = NameGenerator()
        name_generator.save_names_to_csv()
        
        # 2. Exécution du pipeline
        route_namer = RouteNamer(ville, filter_quartier)
        route_namer.load_names()
        route_namer.run_pipeline()
        
        # 3. Création de la carte
        map_generator = MapGenerator(
            route_namer.get_routes_data(), 
            route_namer.get_quartiers_data()
        )
        map_generator.generate_map()
        
        # 4. Résumé
        logger.info(f"Test effectué sur le quartier {filter_quartier}")
        logger.info(f"Routes affichées: {len(route_namer.get_routes_data())} totales")
        logger.info("Processus terminé avec succès !")

        end_time = datetime.datetime.now()
        logger.info(f"{end_time} - Processus terminé en {end_time - start_time}")
        
    except Exception as e:
        logger.error(f"Erreur lors de l'exécution: {e}")
        raise

if __name__ == "__main__":
    main()
