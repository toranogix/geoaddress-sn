"""
Catégories de noms spécifiques par typologie urbaine pour Dakar
"""

CENTRE_VILLE_NAMES = {
    "voies": ["Rue"],
    "personnalites": [
        "Léopold Sédar Senghor", "Abdoulaye Wade", "Blaise Diagne", 
        "El Hadj Malick Sy", "Cheikh Anta Diop", "Aimé Césaire",
        "Nelson Mandela", "Kwame Nkrumah", "Thomas Sankara",
        "Patrice Lumumba", "Ahmadou Bamba", "Cheikh Ibrahima Fall", "Mamadou Dia",
        "Alboury Ndiaye", "Iba Der Thiam"
    ],
    "concepts": [
        "de l'Indépendance", "de la Liberté", "Renaissance", "de la Paix"
    ],
    "lieux_officiels": [
        "Palais", "Assemblée", "Ministère", "Présidence", 
        "Justice", "Commerce", "Finance", "Économie"
    ]
}

MEDINA_NAMES = {
    "voies": ["Rue"],
    "personnalites": [
        "Cheikh Ahmadou Bamba", "Mame Diarra Bousso", "Serigne Touba",
        "Cheikh Ibrahima Fall", "Mame Cheikh Ibrahima Fall", "Mame Diarra", "Seydina Limamou laye"
        "Serigne Modou Kara", "Serigne Bassirou Mbacké", "Serigne Saliou Mbacké", "Lat Ngoné Latir Diop"
    ],
    "concepts": [
        "Teranga", "Fadj", "Jigeen", "Keur", "Touba", "Ndiaga"
    ],
    "lieux_traditionnels": [
        "Mosquée", "Touba", "Médina", "Soumbédioune", "Gorée"
    ]
}

RESIDENTIEL_AISE_NAMES = {
    "voies": ["Rue"],
    "personnalites": [
        "Mariama Ba", "Fatou Diome", "Aminata Sow Fall", "Ken Bugul",
        "Ousmane Sembène", "Cheikh Hamidou Kane", "Boubacar Boris Diop",
        "Aminata Maïga Ka", "Aminata Sow Fall", "Fatou Ndiaye"
    ],
    "concepts": [
        "Horizon", "Aurore", "Crépuscule", "Océan", "Plage",
        "Palmiers", "Baobabs", "Manguiers"
    ],
    "lieux_prestigieux": [
        "Almadies", "Ngor", "Ouakam", "Yoff", "Mermoz", "Fann",
        "Corniche", "Plage", "Océan", "Baie", "Cap", "Pointe"
    ]
}

RESIDENTIEL_POPULAIRE_NAMES = {
    "voies": ["Rue"],
    "personnalites": [
        "Ousmane Sonko", "Bassirou Diomaye Faye", "Waldiodio Ndiaye", "Mame Cheikh Ibrahima Fall",
        "Serigne Modou Kara", "Serigne Bassirou Mbacké", "Serigne Saliou Mbacké",
        "Mame Diarra Bousso", "Cheikh Ibrahima Fall", "Mame Diarra", "Waldiodio Ndiaye"
    ],
    "concepts": [
        "Union", "Paix", "Espoir", "Renaissance"
    ],
    "lieux_communautaires": [
        "École", "Marché", "Mosquée", "Centre", "Place", "Stade"
    ]
}

COMMERCIAL_NAMES = {
    "voies": ["Rue"],
    "personnalites": [
        "Sandaga", "Castors"
    ],
    "concepts": [
        "Commerce", "Marché", "Artisanat", "Boutique", "Étal"
    ],
    "lieux_commerciaux": [
        "Marché", "Boutique", "Étal", "Magasin", "Commerce",
        "Artisanat", "Centre", "Plaza", "Galerie", "Passage"
    ]
}

INDUSTRIEL_NAMES = {
    "voies": ["Rue"],
    "personnalites": [
        "Abdou Diouf", "Léopold Sédar Senghor", "Blaise Diagne", "Cheikh Anta Diop",
    ],
    "concepts": [
        "Industrie", "Port", "Logistique", "Transport", "Entrepôt",
        "Zone", "Terminal", "Quai", "Dock", "Hangar"
    ],
    "lieux_industriels": [
        "Port", "Terminal", "Quai"
    ]
}

TOURISTIQUE_NAMES = {
    "voies": ["Rue"],
    "personnalites": [
        "Mariama Ba", "Baaba Maal", "Ousmane Sembène"
    ],
    "concepts": [
        "Océan", "Plage", "Sable", "Vagues", "Bissap",
        "Palmiers", "Cocotiers", "Baobabs"
    ],
    "lieux_touristiques": [
        "Plage", "Océan", "Corniche", "Baie", "Cap", "Gorée",
        "Phare", "Port", "Marina", "Hôtel"
    ]
}

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
    """Retourne les catégories de noms spécifiques par typologie urbaine

    Args:
        typology (str): Catégories de noms spécifiques par typologie urbaine

    """
    return NAME_CATEGORIES.get(typology, RESIDENTIEL_POPULAIRE_NAMES)
