import time
from borough_finder import BoroughFinder
import pandas as pd

uber_data = pd.read_csv('UberFaresCausInf//uber_updated.csv')

geojson_path = 'UberFaresCausInf//nyc-neighborhoods-2.geojson'  # Adjust the path if necessary
finder = BoroughFinder(geojson_path)

t1 = time.time()
uber_data['pickup_loc'] = uber_data.apply(lambda row: finder.find_location(row['pickup_longitude'], row['pickup_latitude']), axis=1)
uber_data['dropoff_loc'] = uber_data.apply(lambda row: finder.find_location(row['dropoff_longitude'], row['dropoff_latitude']), axis=1)
t2 = time.time()

print(t2-t1)

uber_data.to_csv('updated_uber_loc.csv',index=False)