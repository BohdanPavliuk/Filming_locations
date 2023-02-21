# Filming_locations

This project create map of 10 closest to your cordinates filming location

## How it's working
Script filming_location.py runs only by a terminal, and it requires:
1) Year
2) Your location latitude
3) Your location longtitude
4) Path to location.list file

It's save folium map, named 'map.html' as html file to your working directory 

## Map discription and legend
Map represent not more tham 10 closest filming location and consist of 3 layers:
1) The common background for map with your location marker
2) Markers with name of films, that were filmed here
3) Circlemarkers with distance to this filming location

Legend of map:

<img width="61" alt="Screenshot 2023-02-21 at 23 02 38" src="https://user-images.githubusercontent.com/55399864/220459176-79efcff4-a56d-4786-9d10-3626fbbbe3ea.png"> Your location marker

<img width="49" alt="Screenshot 2023-02-21 at 23 09 55" src="https://user-images.githubusercontent.com/55399864/220459324-f0301f66-60de-4365-9b0f-1aa7c35fcd1d.png"> Marker with a name of film

<img width="47" alt="Screenshot 2023-02-21 at 23 09 48" src="https://user-images.githubusercontent.com/55399864/220459432-38caf63e-8dc2-4cc3-bb99-167093749ef1.png"> Circlemarker with a distance to this filming location

<img width="48" alt="Screenshot 2023-02-21 at 23 26 53" src="https://user-images.githubusercontent.com/55399864/220462223-cd9007ff-eb46-4946-b9ff-26f44df8ca02.png"> To filter your layers

## Example of the script running
Your need to run the script in terminal as a python file with fourth required arguments
It's working not more than 100 seconds and save map to your correct working directory
Or if it's some errors, script will output you a reason of errors

Runned script(year - 2002, location - somewhere in Anlantic ocean):
<img width="762" alt="Screenshot 2023-02-21 at 23 15 55" src="https://user-images.githubusercontent.com/55399864/220460339-1cc75701-0712-4e2a-ae6a-b307f61c21e1.png">

Generated map:
<img width="1035" alt="Screenshot 2023-02-21 at 23 24 23" src="https://user-images.githubusercontent.com/55399864/220461765-1c5154d2-54da-46f3-ab52-813618280c23.png">

P.S. It's better to run script on stable Internet connection and not on WIFI-UCU
