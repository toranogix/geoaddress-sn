"""
Specific name categories by urban typology for Dakar
"""

# Names for Centre-Ville/Plateau categories
CENTRE_VILLE_NAMES = {
    "voies": ["Avenue", "Boulevard", "Place", "Rue"],
    "personnalites": [
        "Léopold Sédar Senghor", "Abdoulaye Wade", "Blaise Diagne", 
        "El Hadj Malick Sy", "Cheikh Anta Diop", "Aimé Césaire",
        "Nelson Mandela", "Kwame Nkrumah", "Thomas Sankara",
        "Patrice Lumumba", "Ahmadou Bamba", "Cheikh Ibrahima Fall"
    ],
    "concepts": [
        "Indépendance", "Liberté", "Démocratie", "Renaissance", 
        "Union", "Paix", "Développement", "Progrès", "Modernité"
    ],
    "lieux_officiels": [
        "Palais", "Assemblée", "Ministère", "Présidence", 
        "Justice", "Commerce", "Finance", "Économie"
    ]
}

# Names for Medina categories
MEDINA_NAMES = {
    "voies": ["Rue", "Impasse", "Place", "Passage"],
    "personnalites": [
        "Cheikh Ahmadou Bamba", "Mame Diarra Bousso", "Serigne Touba",
        "Cheikh Ibrahima Fall", "Mame Cheikh Ibrahima Fall", "Mame Diarra",
        "Serigne Modou Kara", "Serigne Bassirou Mbacké", "Serigne Saliou Mbacké"
    ],
    "concepts": [
        "Teranga", "Fadj", "Jigeen", "Keur", "Ndeup", "Touba", "Ndiaga",
        "Baye", "Mame", "Serigne", "Cheikh", "Imam", "Marabout"
    ],
    "lieux_traditionnels": [
        "Mosquée", "Touba", "Médina", "Soumbédioune", "Gorée", 
        "Marché", "Place", "Cimetière", "École", "Bibliothèque"
    ]
}

# Names for Residential Aisé categories
RESIDENTIEL_AISE_NAMES = {
    "voies": ["Avenue", "Boulevard", "Rue", "Allée", "Villa"],
    "personnalites": [
        "Mariama Ba", "Fatou Diome", "Aminata Sow Fall", "Ken Bugul",
        "Ousmane Sembène", "Cheikh Hamidou Kane", "Boubacar Boris Diop",
        "Aminata Maïga Ka", "Aminata Sow Fall", "Fatou Ndiaye"
    ],
    "concepts": [
        "Horizon", "Étoiles", "Aurore", "Crépuscule", "Océan", "Plage",
        "Palmiers", "Baobabs", "Manguiers", "Cocotiers", "Hibiscus"
    ],
    "lieux_prestigieux": [
        "Almadies", "Ngor", "Ouakam", "Yoff", "Mermoz", "Fann",
        "Corniche", "Plage", "Océan", "Baie", "Cap", "Pointe"
    ]
}

# Names for Residential Populaire categories
RESIDENTIEL_POPULAIRE_NAMES = {
    "voies": ["Rue", "Impasse", "Allée", "Passage"],
    "personnalites": [
        "Ousmane Sonko", "Waldiodio Ndiaye", "Mame Cheikh Ibrahima Fall",
        "Serigne Modou Kara", "Serigne Bassirou Mbacké", "Serigne Saliou Mbacké",
        "Mame Diarra Bousso", "Cheikh Ibrahima Fall", "Mame Diarra"
    ],
    "concepts": [
        "Union", "Paix", "Espoir", "Renaissance", "Développement", "Progrès",
        "Solidarité", "Fraternité", "Communauté", "Famille", "Enfants"
    ],
    "lieux_communautaires": [
        "École", "Marché", "Mosquée", "Centre", "Place", "Stade",
        "Dispensaire", "Bibliothèque", "Jardin", "Parc", "Terrain"
    ]
}

# Names for Commercial categories
COMMERCIAL_NAMES = {
    "voies": ["Rue", "Avenue", "Place", "Marché"],
    "personnalites": [
        "Sandaga", "Castors", "Hysacam", "Marché", "Commerce",
        "Artisan", "Commerçant", "Marchand", "Vendeur"
    ],
    "concepts": [
        "Commerce", "Marché", "Artisanat", "Boutique", "Étal",
        "Vente", "Achat", "Échange", "Négociation", "Affaires"
    ],
    "lieux_commerciaux": [
        "Marché", "Boutique", "Étal", "Magasin", "Commerce",
        "Artisanat", "Centre", "Plaza", "Galerie", "Passage"
    ]
}

# Names for Industrial categories
INDUSTRIEL_NAMES = {
    "voies": ["Route", "Avenue", "Quai", "Zone"],
    "personnalites": [
        "Port", "Industrie", "Logistique", "Transport", "Entrepôt"
    ],
    "concepts": [
        "Industrie", "Port", "Logistique", "Transport", "Entrepôt",
        "Zone", "Terminal", "Quai", "Dock", "Hangar"
    ],
    "lieux_industriels": [
        "Port", "Terminal", "Quai", "Zone", "Entrepôt", "Hangar",
        "Usine", "Atelier", "Dépôt", "Station", "Base"
    ]
}

# Names for Touristique categories
TOURISTIQUE_NAMES = {
    "voies": ["Avenue", "Boulevard", "Corniche", "Route", "Promenade"],
    "personnalites": [
        "Gorée", "Almadies", "Ngor", "Ouakam", "Yoff", "Plage",
        "Océan", "Corniche", "Baie", "Cap", "Pointe"
    ],
    "concepts": [
        "Océan", "Plage", "Sable", "Vagues", "Vent", "Soleil",
        "Palmiers", "Cocotiers", "Baobabs", "Hibiscus", "Fleurs"
    ],
    "lieux_touristiques": [
        "Plage", "Océan", "Corniche", "Baie", "Cap", "Pointe",
        "Phare", "Port", "Marina", "Hôtel", "Résidence", "Villa"
    ]
}

# Mapping of name categories by urban typology
NAME_CATEGORIES = {
    "centre_ville": CENTRE_VILLE_NAMES,
    "plateau": CENTRE_VILLE_NAMES,
    "medina": MEDINA_NAMES,
    "residentiel_aisé": RESIDENTIEL_AISE_NAMES,
    "residentiel_populaire": RESIDENTIEL_POPULAIRE_NAMES,
    "commercial": COMMERCIAL_NAMES,
    "industriel": INDUSTRIEL_NAMES,
    "touristique": TOURISTIQUE_NAMES
}

def get_name_categories(typology: str) -> dict:
    """
    Returns the name categories for a given urban typology
    """
    return NAME_CATEGORIES.get(typology, RESIDENTIEL_POPULAIRE_NAMES)
