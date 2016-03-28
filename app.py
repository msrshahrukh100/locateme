# coding: utf-8
import urllib2
import json
from flask import Flask, render_template
from flask.ext.googlemaps import GoogleMaps
from flask.ext.googlemaps import Map

app = Flask(__name__)
GoogleMaps(app)


##

##

@app.route("/")
def mapview():
  
    sndmap = Map(
        identifier="sndmap",
        lat=37.4419,
        lng=-122.1419,
        style="height:100%;width:100%;top:0;left:0;position:absolute;z-index:200",
        zoom=20,
        markers={'http://maps.google.com/mapfiles/ms/icons/green-dot.png':[(37.4419, -122.1419)],
                 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png':[(37.4300, -122.1400)]},
        
    )
    return render_template('maps.html',sndmap=sndmap)

@app.route("/showmap")
def showmap():
    key1="AIzaSyDYdmM1stbpcYrJaViKBy8RmadEhDw1ygQ"
    key2= "AIzaSyDFhBCrmAUBKOHVLrrMRg5i-YwVnjIy6ZQ" 
	
    url = 'https://maps.googleapis.com/maps/api/place/radarsearch/json?location=28.5611519,77.2808854&radius=5000&name=Masjid&key='+key2
    urlData = urllib2.urlopen(url)
    loadedJson = json.load(urlData)
    items = loadedJson['results']
    coordinates=[]
    for item in items:
        temp = (item['geometry']['location']['lat'] , item['geometry']['location']['lng'])
        coordinates.append(temp)
        # print "The lattitude is : %.14f" % (item['geometry']['location']['lat'])
        # print "The longitude is : %.14f" % (item['geometry']['location']['lng'])
    print coordinates
    pointer = 'http://maps.google.com/mapfiles/ms/icons/green-dot.png'
    marker = {}
    marker[pointer] = coordinates


  
    sndmap = Map(
        identifier="sndmap",
        lat=28.5611519,
        lng=77.2808854,
        style="height:100%;width:100%;top:0;left:0;position:absolute;z-index:200",
        zoom=17,
        markers= marker,#{'http://maps.google.com/mapfiles/ms/icons/green-dot.png':coordinates},
        
    )
    return render_template('maps.html',sndmap=sndmap)

if __name__ == "__main__":
    app.run(debug=True)
