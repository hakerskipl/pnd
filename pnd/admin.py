#-*- coding: utf-8 -*-
from django.contrib import admin
from pnd.models import *

class PlacePhotosInline(admin.TabularInline):
	model = PlacePhotos
	extra = 1

class PlaceMenuInline(admin.TabularInline):
	model = PlaceMenu
	extra = 1

class PlaceAdmin(admin.ModelAdmin):
	list_display = ('name', 'address', 'phone', 'website', 'email')
	search_fields = ('name', 'address')
	filter_horizontal = ('tags',)
	list_filter = ('tags__name',)
	inlines = [
		PlaceMenuInline,
		PlacePhotosInline,
	]

class TagsAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fields = ('name',)

class PlacePhotosAdmin(admin.ModelAdmin):
	list_display = ('place', 'photo')
	ordering = ['place', 'id']
	search_fields = ('place__name',)

class PlaceMenuAdmin(admin.ModelAdmin):
	list_display = ('place', 'name', 'price')
	ordering = ['name']
	search_fields = ('place__name',)

class TodaysIdeaAdmin(admin.ModelAdmin):
	list_display = ('place', 'date', 'slogan')
	search_fields = ('place__name',)
	ordering = ['-date']

admin.site.register(Place, PlaceAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(PlacePhotos, PlacePhotosAdmin)
admin.site.register(PlaceMenu, PlaceMenuAdmin)
admin.site.register(TodaysIdea, TodaysIdeaAdmin)