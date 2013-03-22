#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Place(models.Model):
	TABLES = (
		(1, u'Dwuosobowy'),
		(2, u'Czteroosobowy'),
		(3, u'Szejściosobowy'),
		(4, u'Ośmioosobowy'),
		(5, u'Dziesięcioosobowy lub większy'),
	)

	name = models.CharField(max_length=150)
	desc = models.TextField()
	address = models.CharField(max_length=200)
	hour_open = models.TimeField()
	hour_close = models.TimeField()
	phone = models.CharField(max_length=20)
	email = models.EmailField()
	website = models.URLField()
	table = models.PositiveSmallIntegerField(choices=TABLES)


	def __unicode__(self):
		return u'Lokal ' + self.name

	class Meta:
		verbose_name = u'Lokal'
		verbose_name_plural = u'Lokale'
		ordering = ['name',]

class PlacePhotos(models.Model):
	place = models.ForeignKey('Place')
	photo = models.ImageField(upload_to='/places/')
	desc = models.TextField()

	def __unicode__(self):
		return u'Zdjęcie lokalu ' + self.place.name

	class Meta:
		verbose_name = u'Zdjęcie lokalu'
		verbose_name_plural = u'Zdjęcia lokalu'

class PlaceMenu(models.Model):
	place = models.ForeignKey('Place')
	name = models.CharField(max_length=150)
	desc = models.TextField()
	price = models.CharField(max_length=10)

	def __unicode__(self):
		return self.name + ' w ' + self.place.name

	class Meta:
		verbose_name = u'Pozycja menu'
		verbose_name_plural = u'Pozycje menu'
		ordering = ['place', 'name']
