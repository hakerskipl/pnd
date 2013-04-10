#-*- coding: utf-8 -*-
from django.db import models
from datetime import date
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from autoslug import AutoSlugField

# Create your models here.
class Place(models.Model):
	name = models.CharField(max_length=150, verbose_name=u'Nazwa lokalu')
	slug = AutoSlugField(populate_from='name', unique=True, always_update=True, verbose_name=u'Slug')
	short = models.TextField(null=True, verbose_name=u'Krótki opis')
	desc = models.TextField(null=True, verbose_name=u'Opis')
	address = models.CharField(max_length=200, verbose_name=u'Adres')
	hour_open = models.TimeField(null=True, verbose_name=u'Godzina otwarcia')
	hour_close = models.TimeField(null=True, verbose_name=u'Godzina zamknięcia')
	phone = models.CharField(max_length=20, null=True, verbose_name=u'Telefon')
	email = models.EmailField(null=True, verbose_name=u'Email')
	website = models.URLField(null=True, verbose_name=u'Strona www')
	places_uid = models.TextField(null=True, verbose_name=u'UID Google Places API')
	tags = models.ManyToManyField('Tags', verbose_name=u'Tagi')

	def __unicode__(self):
		return u'Lokal ' + self.name

	class Meta:
		verbose_name = u'Lokal'
		verbose_name_plural = u'Lokale'
		ordering = ['name',]

class Tags(models.Model):
	name = models.CharField(max_length=100, verbose_name=u'Tag')
	icon = models.CharField(max_length=50, verbose_name=u'Klasa CSS ikony')

	def __unicode__(self):
		return u'Tag ' + self.name

	class Meta:
		verbose_name = u'Tag'
		verbose_name_plural = u'Tagi'
		ordering = ['name']

class PlaceTables(models.Model):
	TABLES = (
		(1, u'Dwuosobowy'),
		(2, u'Czteroosobowy'),
		(3, u'Szejściosobowy'),
		(4, u'Ośmioosobowy'),
		(5, u'Dziesięcioosobowy lub większy'),
	)

	place = models.ForeignKey('Place', verbose_name=u'Lokal', related_name='tables')
	table = models.PositiveSmallIntegerField(choices=TABLES, verbose_name=u'Stolik')
	quantity = models.PositiveSmallIntegerField(verbose_name=u'Ilość')

	def __unicode__(self):
		return u'Stoliki w ' + self.place.name

	class Meta:
		verbose_name = u'Stolik'
		verbose_name_plural = u'Stoliki'

class PlacePhotos(models.Model):
	place = models.ForeignKey('Place', verbose_name=u'Lokal', related_name='photos')
	photo = models.ImageField(upload_to='media/places/', verbose_name=u'Zdjęcie')
	photo_thumbnail = ProcessedImageField(upload_to='media/places_thumbnails/', processors=[ResizeToFill(100, 100)], format='JPEG', options={'quality': 80}, verbose_name=u'Miniatura')
	desc = models.TextField(null=True, default=None, verbose_name=u'Opis')

	def __unicode__(self):
		return u'Zdjęcie lokalu ' + self.place.name

	class Meta:
		verbose_name = u'Zdjęcie lokalu'
		verbose_name_plural = u'Zdjęcia lokalu'

class PlaceMenu(models.Model):
	place = models.ForeignKey('Place', verbose_name=u'Lokal', related_name='menu')
	name = models.CharField(max_length=150, verbose_name='Nazwa pozycji')
	desc = models.TextField(verbose_name=u'Opis')
	price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, verbose_name=u'Cena')

	def __unicode__(self):
		return self.name + ' w ' + self.place.name

	class Meta:
		verbose_name = u'Pozycja menu'
		verbose_name_plural = u'Pozycje menu'
		ordering = ['place', 'name']

class TodaysIdea(models.Model):
	place = models.ForeignKey('Place', verbose_name=u'Lokal', related_name='pomysly')
	date = models.DateField(default=date.today(), verbose_name=u'Data projekcji')
	slogan = models.CharField(max_length=150, null=True, default=None, verbose_name=u'Krótki opis (do 150 znaków)')
	photo = ProcessedImageField(upload_to='media/todays_idea/', processors=[ResizeToFill(500, 350)], format='JPEG', options={'quality': 90}, verbose_name=u'Zdjęcie promocyjne', null=True, default=None)

	def __unicode__(self):
		return u'Promocja lokalu ' + self.place.name

	class Meta:
		verbose_name = u'Nasz pomysł'
		verbose_name_plural = u'Nasze pomysły'
		ordering = ['-date']