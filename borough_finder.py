import geopandas as gpd
from shapely.geometry import Point

class BoroughFinder:
    def __init__(self, nyc_json_path):
        """
        Initialize the BoroughFinder with the path to a GeoJSON file containing borough boundaries.
        
        :param geojson_path: Path to the GeoJSON file containing borough boundaries.
        """
        self.boroughs = gpd.read_file(nyc_json_path)
        # self.neighborhoods = gpd.read_file(neighborhood_geojson_path)

    def find_location(self, longitude, latitude):
        """
        Find the location for the given longitude and latitude.
        
        :param longitude: Longitude of the location.
        :param latitude: Latitude of the location.
        :return: The name of the borough, and the exact address of the location if found
        """
        location_point = Point(longitude, latitude)
        
        borough_loc, neighborhood_loc = None, None

        for _, borough in self.boroughs.iterrows():
            if borough['geometry'].contains(location_point):
                # return borough['name']  # Assuming the borough name is in a column called 'name'
                borough_loc = borough['borough']
                neighborhood_loc = borough['neighborhood']
    
        
        if borough_loc is None or neighborhood_loc is None:
            return None
        else:
            return neighborhood_loc, borough_loc


# Example usage (this part would typically be in a separate script or notebook):
if __name__ == "__main__":
    # Initialize the BoroughFinder with the path to your GeoJSON file
    finder = BoroughFinder('UberFaresCausInf//nyc-neighborhoods-2.geojson')
    
    # Test with a sample point
    test_longitude = -73.982169
    test_latitude = 40.761782
    neighborhood, borough = finder.find_location(test_longitude, test_latitude)
    
    if borough and neighborhood:
        print(f"The location ({test_longitude}, {test_latitude}) is in the borough: {borough} and neighborhood: {neighborhood}.")
    else:
        print(f"The location ({test_longitude}, {test_latitude}) is not in any recognized borough.")
