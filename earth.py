#!/home/john/Documentos/Code/anaconda/bin/python
# -*- coding: utf-8 -*-

import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import gmplot

# Descargo los datos desde la página de la Aemet.
#
def getQuakeData():
	# Una URL de prueba de la AEMET
	url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=text&starttime=2010-01-01&endtime=2016-01-01&minmagnitude=5.0"

	headers = {
		'cache-control': "no-cache"
		}

	response = requests.request("GET", url, headers=headers)

	latitudes = []
	longitudes = []

	#print(response.text)
	iterlinea = iter(response.text.splitlines())
	next(iterlinea)
 
	for linea in iterlinea:
		# Saco todas las variables, aunque en realidad sólo hacen falta latitud y longitud.
		EventID,Time,Latitude,Longitude,Depth,Author,Catalog,Contributor,ContributorID,MagType,Magnitude,MagAuthor,EventLocationName = linea.split('|')
		#print(Latitude, Longitude)
		#print(float(Latitude), float(Longitude))
		latitudes.append(float(Latitude))
		longitudes.append(float(Longitude))

	return latitudes, longitudes


def drawQuakes(lats, lons):
	# declare the center of the map, and how much we want the map zoomed in
	gmap = gmplot.GoogleMapPlotter(0, 0, 2)
	# plot heatmap
	gmap.heatmap(lats, lons)
	# Draw
	gmap.draw("quakes_map.html")

latitudes, longitudes = getQuakeData()
drawQuakes(latitudes, longitudes)
