#-*- coding: utf-8 -*-
from django.contrib import admin
from pnd.models import *

class PlaceAdmin(admin.ModelAdmin):
	list_display = ('name', 'address', 'phone', 'website', 'email')
	list_filter = ['table']
	search_fields = ('name', 'address')

class PlacePhotosAdmin(admin.ModelAdmin):
	list_display = ('place', 'photo')
	ordering = ['place', 'pk']
	search_fields = ('place__name',)

class PlaceMenuAdmin(admin.ModelAdmin):
	list_display = ('place', 'name', 'price')
	ordering = ['name']
	search_fields = ('place__name',)

admin.site.register(Place, PlaceAdmin)
admin.site.register(PlacePhotos, PlacePhotosAdmin)
admin.site.register(PlaceMenu, PlaceMenuAdmin)