#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from pnd.models import *

def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

def results(request):
    allPlaces = Place.objects.all()
    return render_to_response('wyniki.html', {'allPlaces': allPlaces}, context_instance=RequestContext(request))

def detail(request, id):
    placeData = Place.objects.get(pk=id)
    return render_to_response('detail.html', {'place': placeData}, context_instance=RequestContext(request))

# Google Place API

import urllib2
from django.utils import simplejson as json
from django.http import HttpResponse
def fetchData(request):
    streets = ['Szeroka', 'Piekary', 'Zeglarska', 'Mostowa', 'Wielkie%20Garbary', 'Prosta', 'Rynek%20Staromiejski', 'Strumykowa', 'Piekary', 'Chelminska', 'Szewska', 'Przedzamcze', 'Kopernika', 'Rabianska', 'Podmurna', 'Prosta', 'Sukiennicza', 'Wysoka', 'Rynek%20Nowomiejski']
    response = u''
    for city in streets:
        i = 0
        response = response + u'<br><br><b>Ulica: ' + city + u'</b><br><br>'
        request_url = "http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=" + city + ",Torun,Poland"
        city_req = urllib2.Request(request_url)
        city_opener = urllib2.build_opener()
        city_f = city_opener.open(city_req)
        city_data = json.load(city_f)

        search_types = ['keyword', 'name', 'type']
        for st in search_types:
            if st == 'type':
                keywords = ['art_gallery', 'cafe', 'movie_theater', 'lodging', 'food', 'museum', 'night_club', 'restaurant', 'zoo']
            else:
                keywords = ['restauracja', 'bar', 'pub', 'pizzeria', 'grill']
            response = response + u'<br>Typ szukania: <i>' + st + u'</i><br>'
            for word in keywords:
                req_url = "https://maps.googleapis.com/maps/api/place/search/json?location=" + str(city_data['results'][0]['geometry']['location']['lat']) + "," + str(city_data['results'][0]['geometry']['location']['lng']) + "&radius=50&language=pl&"
                if st == 'type':
                    req_url = req_url + "types=" + word
                else:
                    if st == 'keyword':
                        req_url = req_url + "keyword=" + word
                    else:
                        req_url = req_url + "name=" + word
                req_url = req_url + "&sensor=false&key=AIzaSyDDOcaI9GNdrmjoBTviEfIKU86U1QqxnBk"
                response = response + u'<br>Słowo kluczowe: <i>' + word + u'</i><br><br>' + u'URL zapytania: ' + req_url + u'<br><br>'
                req = urllib2.Request(req_url)
                opener = urllib2.build_opener()
                f = opener.open(req)
                data = json.load(f)               
                resp = insertFetchData(data)
                response = response + resp
    return HttpResponse(response)

def insertFetchData(data):
    response = u''
    for data in data['results']:
        response = response + u'Lokal ' + data['name'] + u'<br>' + u'ID: ' + data['id'] + u'<br>'
        if (Place.objects.filter(places_uid__contains = data['id']).count() <= 0):
            response = response + u'Test ID: ' + str(Place.objects.filter(places_uid__contains = data['id']).count()) + u'<br>'
            new = Place(name=data['name'], 
                desc=None,
                address=None,
                hour_open=None,
                hour_close=None,
                phone=None,
                email=None,
                website=None,
                places_uid=data['id']
                )
            
           
            req2 = urllib2.Request("https://maps.googleapis.com/maps/api/place/details/json?key=AIzaSyDDOcaI9GNdrmjoBTviEfIKU86U1QqxnBk&sensor=false&language=pl&reference=" + data['reference'])
            opener2 = urllib2.build_opener()
            f2 = opener2.open(req2)
            data2 = json.load(f2)
            
            try:
                new.address = data2['result']['formatted_address']
            except:
                try:
                    new.address = data2['result']['vicinity']
                except:
                    pass
            try:
                new.phone = data2['result']['formatted_phone_number']
            except:
                pass
            try:
                new.website = data2['result']['website']
            except:
                pass
            try:
                new.hour_open = data2['opening_hours']['periods']['open']['time']
            except:
                pass
            try:
                new.hour_close = data2['opening_hours']['periods']['close']
            except:
                pass
            new.save()
            
            # Zdjęcia
            
            from django.core.files import File
            from django.core.files.temp import NamedTemporaryFile
            from urlparse import urlparse

            img_temp = NamedTemporaryFile(delete=True)
            
            try:
                for pht in data2['result']['photos']:

                    photoRequestURL = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=1600&key=AIzaSyDDOcaI9GNdrmjoBTviEfIKU86U1QqxnBk&sensor=false&photoreference=" + pht['photo_reference']
                    name = urlparse(photoRequestURL).path.split('/')[-1] + ".jpg"

                    img_temp.write(urllib2.urlopen(photoRequestURL).read())
                    img_temp.flush()
                    
                    new_photo = PlacePhotos(
                        place=new,
                        photo=None,
                        desc=None
                    )

                    new_photo.photo.save(name, File(img_temp), save=False)
                    
                    new_photo.save()
            except:
                pass
            
            response = response + u'Dodane: <b>' + new.name + u'</b>  ' + str(new.id) + u'<br><br>'
    return response