"""Module create html map for filming locations
Also it get all argument from command line
There are 4 required arguments
First - year, second - latitude, third - longitude, fourth - path to .list file"""
import time
import re
import argparse
from haversine import haversine
from geopy.geocoders import Nominatim
import folium




def read_location(path: str, year: int) -> list:
    """Function get path to file, where film location is and a year 
    of files you want to locate and return list, where all found file 
    found during 100 second are
    >>> read_location('dwwadwa.dawdaw', 2021)
    Sorry, your file not found
    >>> read_location('location.list', 1111)
    This year is not supported
    """
    if not (isinstance(path,str) and isinstance(year, int)):
        return None
    if  not 1900 <= year <= 2023:
        print('This year is not supported')
        return None
    time_spend = 0
    start = time.time()
    result = []
    locations = []
    geolocator = Nominatim(user_agent="location")
    try:
        with open(path, encoding='latin1') as file:

            for line in file.readlines():

                end = time.time()
                time_spend += end - start
                if time_spend >= 100:
                    break
                start = time.time()

                try:
                    if f'({year})' not in line:
                        continue

                    line = line[:-1].split('\t')

                    if '(' in line[-1]:
                        if line[-2] in locations:
                            continue
                        get_loc = line[-2]
                    else:
                        if line[-1] in locations:
                            continue
                        get_loc = line[-1]

                    location = geolocator.geocode(get_loc)

                    if location:
                        locations.append(get_loc)
                        result.append((line[0], location.latitude, location.longitude, get_loc))
                        # print(len(result))
                except:
                    continue
            file.close()
    except FileNotFoundError:
        print("Sorry, your file not found")
        return None
    return result

def create_map(film_location: list, your_location: list):
    """Function get list of films and tuple of your location and
    create html folium map, where at max 10 the closest films are and also marker of
    your location
    >>> create_map([], [30.25, -10.2123])
    Sorry, no film founds
    >>> create_map([('Name', 30.2312, 12.431212, 'Los Angeles, California, USA')], ['hey', 'you'])
    """
    if not (isinstance(film_location, list) and isinstance(your_location, list)):
        return
    if not film_location:
        return
    if any(not isinstance(i, float) for i in your_location):
        return
    if not(-90 <= your_location[0] <= 90 and -180 <= your_location[1] <= 180):
        return
    film_location = sorted(film_location, key=lambda x:\
         haversine((your_location[0], your_location[1]), (x[1],x[2])))[:10]
    film_map = folium.Map(tiles="Stamen Terrain")
    fg_name = folium.FeatureGroup(name="Name of the closest film location")
    fg_dist = folium.FeatureGroup(name="Distant from your location to filming location")
    film_map.add_child(folium.Marker(location=your_location, popup = 'Your location',\
         icon=folium.Icon(color='lightgray', icon='home', prefix='fa')))
    for i in film_location:
        name = re.findall('".+"', i[0])[0]
        distant = round(haversine((your_location[0], your_location[1]), (i[1],i[2])), 2)
        fg_name.add_child(folium.Marker(location = [i[1], i[2]],\
             popup=name, icon=folium.Icon(color='blue', icon='film', prefix='fa')))
        fg_dist.add_child(folium.CircleMarker(location = [i[1], i[2]],\
             radius = 10, popup=f'{distant} km', fill_color= 'purple',color='red',fill_opacity=0.5))
    film_map.add_child(fg_name)
    film_map.add_child(fg_dist)
    film_map.add_child(folium.LayerControl())
    film_map.save('map.html')

def main(path, year, latitude,  longitude):
    """Main function of module, which get all needed information,
    create html map and save it to your working directory
    >>> main(2312, '321', 2312, 3213)
    input uncorect data
    >>> main('location.list', 2021, -133.00,  1444.00)
    Your cordinates isn't on Earth
    """

    if not (isinstance(path, str) and isinstance(year, int)\
         and isinstance(latitude, float) and isinstance(longitude, float)):
        print('input uncorect data')
        return
    if  not (-90 <= latitude <= 90 and -180 <= longitude <= 180):
        print("Your cordinates isn't on Earth")
        return
    read_locations = read_location(path, year)
    create_map(read_locations, [latitude, longitude])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create map of filming location')

    parser.add_argument('year', type = int,  help= 'Year of filming location')
    parser.add_argument('latitude', type = float,  help= 'Your correct latitude')
    parser.add_argument('longitude', type = float,  help= 'Your correct longitude')
    parser.add_argument('path', type = str,  help = "path to file")

    args = parser.parse_args()
    main(args.path, args.year, args.latitude, args.longitude)
    # import doctest
    # print(doctest.testmod())
