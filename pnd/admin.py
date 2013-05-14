#-*- coding: utf-8 -*-
from django.contrib import admin
from django.db.models import Count
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
	fieldsets = (
        (None, {
            'fields': ('name', 'desc', 'tags')
        }),
        ('Dane teleadresowe', {
        	'fields': ('phone', 'website', 'fb', 'email')
        	}),
        ('Godziny otwarcia', {
            'classes': ('collapse',),
            'fields': ('mon_hour_open', 'mon_hour_close', 'tue_hour_open', 'tue_hour_close', 'wed_hour_open', 'wed_hour_close', 'thr_hour_open', 'thr_hour_close', 'fri_hour_open', 'fri_hour_close', 'sat_hour_open', 'sat_hour_close', 'sun_hour_open', 'sun_hour_close')
        })
    )
	inlines = [
		PlaceMenuInline,
		PlacePhotosInline,
	]
	class Media:
		js = [
			'/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
			'/static/js/tinymce.init.js',
		]

class TagsAdmin(admin.ModelAdmin):
	list_display = ('name', 'num_places_count', 'icon')
	search_fields = ('name',)

	def queryset(self, request):
		qs = super(TagsAdmin, self).queryset(request)
		return qs.annotate(num_places=Count('place__id'))

	def num_places_count(self, obj):
		return obj.num_places
	num_places_count.short_description = 'Ilość lokali'
	num_places_count.admin_order_field = 'num_places'

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

class NewsletterAdmin(admin.ModelAdmin):
	list_display = ('imie', 'email',)
	search_fields = ('email',)

admin.site.register(Place, PlaceAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(PlacePhotos, PlacePhotosAdmin)
admin.site.register(PlaceMenu, PlaceMenuAdmin)
admin.site.register(TodaysIdea, TodaysIdeaAdmin)
admin.site.register(Newsletter, NewsletterAdmin)

from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin
#Flatpages
class FlatPageAdmin(FlatPageAdmin):
	class Media:
		js = [
			'/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
			'/static/js/tinymce.init.js',
		]

# We have to unregister it, and then reregister
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)