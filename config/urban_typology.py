"""Typologie urbaine de Dakar
"""

URBAN_TYPOLOGIES = {
    "centre_ville": {
        "name": "Centre-Ville",
        "description": "Zone administrative et commerciale centrale",
        "characteristics": ["administratif", "commercial", "bureaux", "gouvernement"],
        "route_types": ["Rue"],
        "naming_style": "officiel"
    },
    "plateau": {
        "name": "Plateau",
        "description": "Quartier d'affaires et administratif",
        "characteristics": ["affaires", "administratif", "bureaux", "banques"],
        "route_types": ["Rue"],
        "naming_style": "officiel"
    },
    "medina": {
        "name": "Médina",
        "description": "Quartier historique et traditionnel",
        "characteristics": ["historique", "traditionnel", "culturel", "religieux"],
        "route_types": ["Rue"],
        "naming_style": "traditionnel"
    },
    "residentiel_aisé": {
        "name": "Résidentiel Aisé",
        "description": "Quartiers résidentiels de standing",
        "characteristics": ["résidentiel", "villas", "standing", "calme"],
        "route_types": ["Rue"],
        "naming_style": "prestigieux"
    },
    "residentiel_populaire": {
        "name": "Résidentiel Populaire",
        "description": "Quartiers résidentiels populaires",
        "characteristics": ["résidentiel", "populaire", "familial", "communautaire"],
        "route_types": ["Rue"],
        "naming_style": "communautaire"
    },
    "commercial": {
        "name": "Commercial",
        "description": "Zones commerciales et marchés",
        "characteristics": ["commercial", "marché", "commerce", "artisanat"],
        "route_types": ["Rue"],
        "naming_style": "commercial"
    },
    "industriel": {
        "name": "Industriel",
        "description": "Zones industrielles et portuaires",
        "characteristics": ["industriel", "portuaire", "logistique", "entrepôts"],
        "route_types": ["Rue"],
        "naming_style": "fonctionnel"
    },
    "touristique": {
        "name": "Touristique",
        "description": "Zones touristiques et côtières",
        "characteristics": ["touristique", "plage", "hôtels", "restaurants"],
        "route_types": ["Rue"],
        "naming_style": "attractif"
    }
}

DAKAR_QUARTERS_TYPOLOGY = {
    # Centre-ville et Plateau
    "plateau": "centre_ville",
    "centre": "centre_ville",
    "kermel": "centre_ville",
    
    # Médina et quartiers historiques
    "medina": "medina",
    "soumbédioune": "medina",
    "gorée": "medina",
    
    # Résidentiel aisé
    "almadies": "residentiel_aisé",
    "ngor": "residentiel_aisé",
    "ouakam": "residentiel_aisé",
    "yoff": "residentiel_aisé",
    "mermoz": "residentiel_aisé",
    "sacré-coeur": "residentiel_aisé",
    "fann": "residentiel_aisé",
    "hann": "residentiel_aisé",
    
    # Résidentiel populaire
    "pikine": "residentiel_populaire",
    "guédiawaye": "residentiel_populaire",
    "parcelles-assainies": "residentiel_populaire",
    "thiaroye": "residentiel_populaire",
    "keur-massar": "residentiel_populaire",
    
    # Commercial
    "sandaga": "commercial",
    "castors": "commercial",
    
    # Industriel/Portuaire
    "port": "industriel",
    "bel-air": "industriel",
    
    # Touristique
    "corniche": "touristique",
    "plage": "touristique"
}

def get_urban_typology(quarter_name: str) -> str:
    """Retourne la typologie urbaine d'un quartier

    Args:
        quarter_name (str): Nom du quartier

    Returns:
        str: Typologie urbaine
    """
    quarter_lower = quarter_name.lower().strip()
    
    if quarter_lower in DAKAR_QUARTERS_TYPOLOGY:
        return DAKAR_QUARTERS_TYPOLOGY[quarter_lower]
    
    for quarter_key, typology in DAKAR_QUARTERS_TYPOLOGY.items():
        if quarter_key in quarter_lower or quarter_lower in quarter_key:
            return typology
    
    # Par défaut, résidentiel populaire
    return "residentiel_populaire"

def get_typology_config(typology: str) -> dict:
    """Retourne la configuration d'une typologie urbaine

    Args:
        typology (str): Typologie urbaine

    Returns:
        dict: Configuration de la typologie urbaine
    """
    return URBAN_TYPOLOGIES.get(typology, URBAN_TYPOLOGIES["residentiel_populaire"])
