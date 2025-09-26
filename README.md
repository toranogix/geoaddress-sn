# 🗺️ Projet de Nommage des Rues

Attribue automatiquement des noms aux rues d'un quartier en utilisant des données OpenStreetMap et génère une carte interactive.

## 📁 Fichiers

- `main.py` - Script principal pour tout exécuter
- `name_generator.py` - Gère les noms de rues
- `route_namer.py` - Télécharge et traite les routes
- `map_generator.py` - Crée des cartes interactives

## 🚀 Démarrage Rapide

```bash
python main.py
```

Cela va :
1. Générer une liste de noms de rues
2. Télécharger les routes depuis OpenStreetMap pour Yoff, Dakar comme test. Vous pouvez le changer ensuite
3. Attribuer des noms aux routes
4. Créer une carte interactive (`carte_test.html`)

## ⚙️ Configuration

Modifiez `main.py` pour changer :
- `ville` - Ville cible (par défaut : "Dakar, Senegal")
- `quartier_test` - Quartier (par défaut : "Yoff")

## 📦 Installation

```bash
pip install osmnx geopandas pandas folium
```

## 📊 Sortie

- `names.csv` - Liste des noms de rues
- `routes_quartier_test.geojson` - Routes téléchargées
- `quartier_test.geojson` - Limite du quartier
- `carte_test.html` - Carte interactive

## 🎯 Fonctionnalités

- Télécharge des données réelles de rues depuis OpenStreetMap
- Attribue des noms prédéfinis aux rues
- Crée des cartes interactives optimisées
- Gère efficacement les gros jeux de données


## 🆘 Problèmes ?

- Vérifiez votre connexion internet
- Assurez-vous que le nom du quartier existe dans OpenStreetMap
- Essayez un nom de quartier différent

## Contributions

N'hésitez pas à faire un pull du repo ou à donner votre avis !

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.



