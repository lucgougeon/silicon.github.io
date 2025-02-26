import folium

def create_kumamoto_map():
    """
    Creates a Folium map centered on Kumamoto City, Japan.

    Returns:
        folium.Map: A Folium map object.
    """

    # Coordinates for the center of Kumamoto City (approximate)
    kumamoto_latitude = 32.8032
    kumamoto_longitude = 130.7083

    # Create a map object
    kumamoto_map = folium.Map(
        location=[kumamoto_latitude, kumamoto_longitude],
        zoom_start=12,  # Adjust zoom level as needed
        tiles="OpenStreetMap", # You can change tiles options, e.g. "Stamen Terrain" or "Stamen Toner"
    )

    # Optional: Add a marker for Kumamoto Castle (a famous landmark)
    kumamoto_castle_latitude = 32.8054
    kumamoto_castle_longitude = 130.7095
    folium.Marker(
        [kumamoto_castle_latitude, kumamoto_castle_longitude],
        popup="Kumamoto Castle",
        icon=folium.Icon(color="red", icon="castle", prefix="fa"), # Using a castle icon
    ).add_to(kumamoto_map)

    return kumamoto_map

# Create the map
kumamoto_map = create_kumamoto_map()

# Save the map to an HTML file (optional)
kumamoto_map.save("kumamoto_city_map.html")

# Display the map in a Jupyter Notebook (if applicable)
# If you are using a Jupyter Notebook, uncomment the line below.
# kumamoto_map
