#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import sys
import os
import bs4
import requests

citeName = "http://fallingrain.com/"

class CityData:

    def __init__(self):
        self.name = ""
        self.population = -9999
        self.lat = -9999
        self.lon = -9999

    def __str__(self):
        s = ""
        s += "City name: {0}\n".format(self.name.encode("utf-8"))
        s += "\tlon: {0}\n".format(self.lon)
        s += "\tlat :{0}\n".format(self.lat)
        s += "\tpopulation: {0}\n".format(self.population)
        return s


def getCityName(pageData):
    h1=pageData.select('h3')
    if(len(h1) == 0):
        return "123"
    cityName=h1[0].getText()
    cityName = cityName.replace(" ", "").split(":")[-1]
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
    return population


def parseCityData(pathToPage):
    s=requests.get(pathToPage)
    pageData=bs4.BeautifulSoup(s.text, "html.parser")
    currCity = CityData()
    currCity.name = getCityName(pageData)
    cityCoord = getCityCoord(pageData)
    currCity.lat = cityCoord["lat"]
    currCity.lon = cityCoord["lon"]
    currCity.population = getCityPopulation(pageData)
    return currCity

def parseLetterData(pathToLetter):
    s=requests.get(pathToLetter)
    pageData=bs4.BeautifulSoup(s.text, "html.parser")
    linesInTable = pageData.find("table").find_all('tr')
    linesInTable = linesInTable[1:]
    for line in linesInTable:
        linkData = line.find("td").find("a")
        linkToCity = linkData.get('href')
        currCity = parseCityData(citeName+linkToCity)
        print currCity
    return

def main():
    #parseRegionData("http://fallingrain.com/world/TU/32/")
    parseLetterData("http://fallingrain.com/world/TU/32/a/R/")
    parseCityData('http://fallingrain.com/world/TU/78/Sahinler_Mahallesi.html')

    print "Done!"
    return 

if __name__ == "__main__":	  
    sys.exit(main())
