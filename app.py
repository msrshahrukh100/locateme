# coding: utf-8
import urllib2
import json
from flask import Flask, render_template,jsonify,request,session
from flask.ext.googlemaps import GoogleMaps
from flask.ext.googlemaps import Map

app = Flask(__name__)
GoogleMaps(app)

app.config['SECRET_KEY'] = 'whattokeepsecret!'
##

##

@app.route("/")
def mapview():
    return render_template('index.html')




@app.route("/storelocations",methods=['POST','GET'])
def storelocation():
    x=77.2824813
    y=28.5650987
    session['longitude'] = request.json.get('longitude',x )
    session['lattitude'] = request.json.get('lattitude',y)

    return jsonify(msg="Stored")



@app.route("/showmap/<int:id>")
def showmap(id):
    key1="AIzaSyDYdmM1stbpcYrJaViKBy8RmadEhDw1ygQ"
    key2= "AIzaSyDFhBCrmAUBKOHVLrrMRg5i-YwVnjIy6ZQ"
    key = "AIzaSyBtx9Omz3nwwzCgG6jCj_PJXKQNEi8t_Ac" 
    latt = str(session['lattitude'])
    lon = str(session['longitude'])
    value = ""
    place = ""
    if id == 1:
        place = "Bus Stop"
        value =  "Bus+Stop"
        print "bs"
    if id == 2:
        place = "Hotels and Restaurants"
        value = "Hotels+Restaurants"
    if id == 3:
        place = "Masjid"
        value = "Masjid"
    if id == 4:
        place = "School and College"
        value = "School+College"
    if id == 5:
        place = "Hospital"
        value = "Hospital"
    if id == 6:
        place = "Metro Station"
        value = "Metro+Station"
    if id == 7:
        place = "Railway Station"
        value = "Railway+Station"
	
    url = 'https://maps.googleapis.com/maps/api/place/radarsearch/json?location='+latt+','+lon+'&radius=5000&name='+value+'&key='+key
    urlData = urllib2.urlopen(url)
    loadedJson = json.load(urlData)
    items = loadedJson['results']
    coordinates=[]
    for item in items:
        temp = (item['geometry']['location']['lat'] , item['geometry']['location']['lng'])
        coordinates.append(temp)

    pointer1 = 'http://maps.google.com/mapfiles/ms/icons/green-dot.png'
    pointer2 = 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png'
    marker = {}
    marker[pointer1] = coordinates
    marker[pointer2] = [(latt,lon)]



  
    sndmap = Map(
        identifier="sndmap",
        lat=latt,
        lng=lon,
        style="height:100%;width:100%;top:7%;left:0;position:absolute;z-index:200",
        zoom=18,
        markers= marker,#{'http://maps.google.com/mapfiles/ms/icons/green-dot.png':coordinates},
        
    )
    return render_template('maps.html',sndmap=sndmap,place=place)

if __name__ == "__main__":
    app.run(debug=True)
