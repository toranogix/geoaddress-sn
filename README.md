# 🗺️ Street Naming Project

Automatically assigns names to streets in a neighborhood using OpenStreetMap and generates an interactive map.

## 📁 Files

- `launch.py` - Main script to run everything
- `name_generator.py` - Manages street names
- `route_namer.py` - Downloads and processes routes
- `map_generator.py` - Creates interactive maps

## 🚀 Quick Start

```bash
python launch.py
```

This will:
1. Generate a list of street names
2. Download routes from OpenStreetMap for Yoff, Dakar as a test. You can change it afterwards
3. Assign names to the routes
4. Create an interactive map (`carte_test.html`)

## ⚙️ Configuration

Edit `main.py` to change:
- `ville` - Target city (default: "Dakar, Senegal")
- `quartier_test` - Neighborhood (default: "Yoff")

## 📦 Install

```bash
pip install osmnx geopandas pandas folium
```

## 📊 Output

- `names.csv` - List of street names
- `routes_quartier_test.geojson` - Downloaded routes
- `quartier_test.geojson` - Neighborhood boundary
- `carte_test.html` - Interactive map

## 🎯 Features

- Downloads real street data from OpenStreetMap
- Assigns predefined names to streets
- Creates optimized interactive maps
- Handles large datasets efficiently


## 🆘 Issues?

- Check your internet connection
- Make sure the neighborhood name exists in OpenStreetMap
- Try a different neighborhood name

## Contributions

Feel free to pull the repo or give some feedback!


**Happy mapping! 🗺️**

