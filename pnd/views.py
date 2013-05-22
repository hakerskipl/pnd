#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.db.models import Q
from django.utils import simplejson as json
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.db.models import Count
from datetime import date
import random
from pnd.models import *
from pnd.forms import *

def index(request, home=False):
    today = date.today()
    try:
        todaysIdea = TodaysIdea.objects.get(date__exact=today)
    except:
        todaysIdea = None
    tagsHome = Tags.objects.filter(home=True)
    tagsExtra = None
    tagsLess = None
    if home:
        tagsExtra = Tags.objects.exclude(home=True).annotate(num_places=Count('place__id')).filter(num_places__gt=5).order_by('-num_places')
        tagsLess = Tags.objects.exclude(home=True).annotate(num_places=Count('place__id')).filter(num_places__lte=5).order_by('-num_places')
    return render_to_response('index.html', {'idea':todaysIdea, 'tags':tagsHome, 'tagsExtra': tagsExtra, 'tagsLess': tagsLess, 'home':not home}, context_instance=RequestContext(request))

def results(request, slug):
    tag = Tags.objects.get(slug__exact=slug)
    allPlaces = Place.objects.filter(tags__slug__exact=slug)
    return render_to_response('wyniki.html', {'allPlaces': allPlaces, 'tag':tag}, context_instance=RequestContext(request))

def detail(request, slug):
    placeData = Place.objects.get(slug=slug)
    return render_to_response('new-detail.html', {'place': placeData}, context_instance=RequestContext(request))

def search(request):
    if request.method == 'POST':
        #Szukanie
        form = SearchForm(request.POST)
        if form.is_valid():
            results = Place.objects.filter(Q(name__icontains=form.cleaned_data['szukaj']) | Q(address__icontains=form.cleaned_data['szukaj']))
            return render_to_response('wyniki.html', {'allPlaces': results, 'keyword': form.cleaned_data['szukaj']}, context_instance=RequestContext(request))
        else:
            return redirect('index')
    else:
        return redirect('index')

def feelLucky(request):
    random.seed()
    number_of_records = Place.objects.count()
    random_index = int(random.random()*number_of_records)+1
    place = Place.objects.get(pk=random_index)
    return redirect('detail', place.slug)

def helpUs(request):
    return render_to_response('help-us.html', context_instance=RequestContext(request))

def newsletterSignUp(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            signUp = Newsletter(imie=form.cleaned_data['imie'], email=form.cleaned_data['email'])
            signUp.save()
            return HttpResponse(json.dumps({'answer':1}), mimetype="application/json")
        else:
            jsonResponse = {'imie': form['imie'].errors, 'email': form['email'].errors}
            return HttpResponse(json.dumps(jsonResponse), mimetype="application/json")
    else:
        return HttpResponse(json.dumps({'answer':0}), mimetype="application/json")


class Error404(TemplateView):
    template_name = "404.html"

class Error500(TemplateView):
    template_name = "500.html"

# Google Place API

import urllib2
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
                keywords = ['night_club', 'restaurant', 'cafe', 'art_gallery',  'movie_theater', 'lodging', 'food', 'museum', 'zoo']
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
            
            try:
                for pht in data2['result']['photos']:

                    response = response + u"<br>Zdjęcie: " + pht['photo_reference'] + u"<br>"

                    photoRequestURL = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=1600&key=AIzaSyDDOcaI9GNdrmjoBTviEfIKU86U1QqxnBk&sensor=false&photoreference=" + pht['photo_reference']
                    name = urlparse(photoRequestURL).path.split('/')[-1] + ".jpg"

                    img_temp = NamedTemporaryFile(delete=True)
                    img_temp.write(urllib2.urlopen(photoRequestURL).read())
                    img_temp.flush()
                    
                    new_photo = PlacePhotos(
                        place=new,
                        photo=None,
                        photo_thumbnail=None,
                        desc=None
                    )

                    new_photo.photo.save(name, File(img_temp), save=False)
                    new_photo.photo_thumbnail.save(name, File(img_temp), save=False)
                    
                    new_photo.save()
            except:
                pass
            
            
            response = response + u'Dodane: <b>' + new.name + u'</b>  ' + str(new.id) + u'<br><br>'
    return response