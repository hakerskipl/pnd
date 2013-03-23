#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from pnd.models import *

def index(request):
	return render_to_response('index.html', context_instance=RequestContext(request))

def results(request):
	return render_to_response('wyniki.html', context_instance=RequestContext(request))

def detail(request):
	return render_to_response('detail.html', context_instance=RequestContext(request))

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
        keywords = ['restauracja', 'bar', 'pub', 'pizzeria', 'grill']
        request_url = "http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=" + city + ",Torun,Poland"
        city_req = urllib2.Request(request_url)
        city_opener = urllib2.build_opener()
        city_f = city_opener.open(city_req)
        city_data = json.load(city_f)
        for word in keywords:
            req_url = "https://maps.googleapis.com/maps/api/place/search/json?location=" + str(city_data['results'][0]['geometry']['location']['lat']) + "," + str(city_data['results'][0]['geometry']['location']['lng']) + "&radius=50&language=pl&name=" + word + "&sensor=false&key=AIzaSyDDOcaI9GNdrmjoBTviEfIKU86U1QqxnBk"
            response = response + u'URL zapytania: ' + req_url + u'<br><br>'
            req = urllib2.Request(req_url)
            opener = urllib2.build_opener()
            opener2 = urllib2.build_opener()
            f = opener.open(req)
            data = json.load(f)
            try:
                response = response + u'Token: ' + data['next_page_token'] + u'<br><br>' 
            except:
                pass
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
                    
                    try:
                        req2 = urllib2.Request("https://maps.googleapis.com/maps/api/place/details/json?key=AIzaSyDDOcaI9GNdrmjoBTviEfIKU86U1QqxnBk&sensor=false&reference=" + data['reference'])
                        f2 = opener2.open(req2)
                        data2 = json.load(f2)
                        
                        try:
                            new.address = data2['result']['formatted_address']
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
                    except:
                        pass
                    i = i +1
                    new.save()
                    response = response + u'Dodane: <b>' + new.name + u'</b>  ' + str(new.id) + u'<br><br>'
    return HttpResponse(response)