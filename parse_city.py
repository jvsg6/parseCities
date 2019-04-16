#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import sys
import os
import bs4
import requests


def getCityName(pageData):
    h1=pageData.select('h1')
    cityName=h1[0].getText()
    return cityName

def getCityCoord(pageData):
    coordLine = pageData.find("table").find_all('td')
    lat = float(coordLine[0].getText())
    lon = float(coordLine[1].getText())
    return {"lat": lat, "lon": lon}

def getCityPopulation(pageData):
    coordLine = pageData.find("table").find_all('td')
    populationSetting = coordLine[11].getText()
    population = float(populationSetting.replace(" ", "").split(":")[-1])
    print population
    return population


def parseCityData(pathToPage):
    s=requests.get(pathToPage)
    pageData=bs4.BeautifulSoup(s.text, "html.parser")
    cityName = getCityName(pageData)
    cityCoord = getCityCoord(pageData)
    cityPop = getCityPopulation(pageData)



def main():
    parseCityData('http://fallingrain.com/world/TU/78/Sahinler_Mahallesi.html')

    print "Done!"
    return 

if __name__ == "__main__":	  
    sys.exit(main())
