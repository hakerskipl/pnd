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

def fetchData(request, id):
    city = Miasta.objects.get(pk=id)
    i = 0
    keywords = ['serwis%20samochodowy', 'warsztat%20samochodowy', 'naprawa%20samochodów', 'serwis%20samochodów', 'lakiernictwo', 'blacharstwo%20samochodowe', 'mechanika%20pojazdowa',  'auto%20serwis']
    city_req = urllib2.Request("http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=" + city.name + ",Poland")
    city_opener = urllib2.build_opener()
    city_f = city_opener.open(city_req)
    city_data = json.load(city_f)
    for word in keywords:
        req = urllib2.Request("https://maps.googleapis.com/maps/api/place/search/json?location=" + str(city_data['results'][0]['geometry']['location']['lat']) + "," + str(city_data['results'][0]['geometry']['location']['lng']) + "&radius=15000&language=pl&name=" + word + "&sensor=false&key=AIzaSyDDOcaI9GNdrmjoBTviEfIKU86U1QqxnBk")
        opener = urllib2.build_opener()
        opener2 = urllib2.build_opener()
        f = opener.open(req)
        data = json.load(f)
        for data in data['results']:
            if (Warsztaty.objects.filter(places_uid__contains = data['id']).count() <= 0):
                new = Warsztaty(name=data['name'], location=data['vicinity'], places_id=data['reference'], places_uid=data['id'])
                new.save()
                i = i +1
                try:
                    req2 = urllib2.Request("https://maps.googleapis.com/maps/api/place/details/json?key=AIzaSyDDOcaI9GNdrmjoBTviEfIKU86U1QqxnBk&sensor=false&reference=" + new.places_id)
                    f2 = opener2.open(req2)
                    data2 = json.load(f2)
                    try:
                        new.phone = data2['result']['formatted_phone_number']
                    except:
                        pass
                    try:
                        new.website = data2['result']['website']
                    except:
                        pass
                    try:
                        new.rating = data2['result']['rating']
                    except:
                        pass
                    new.save()
                except:
                    pass
    return HttpResponse('OK.' + str(i))