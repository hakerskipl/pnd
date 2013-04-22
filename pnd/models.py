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
	desc = models.TextField(null=True, blank=True, verbose_name=u'Opis')
	address = models.CharField(max_length=200, verbose_name=u'Adres')
	# Godziny otwarcia
	mon_hour_open = models.TimeField(null=True, blank=True, verbose_name=u'Godzina otwarcia (Pon)')
	mon_hour_close = models.TimeField(null=True, blank=True, verbose_name=u'Godzina zamknięcia (Pon)')
	tue_hour_open = models.TimeField(null=True, blank=True, verbose_name=u'Godzina otwarcia (Wto)')
	tue_hour_close = models.TimeField(null=True, blank=True, verbose_name=u'Godzina zamknięcia (Wto)')
	wed_hour_open = models.TimeField(null=True, blank=True, verbose_name=u'Godzina otwarcia (Śro)')
	wed_hour_close = models.TimeField(null=True, blank=True, verbose_name=u'Godzina zamknięcia (Śro)')
	thr_hour_open = models.TimeField(null=True, blank=True, verbose_name=u'Godzina otwarcia (Czw)')
	thr_hour_close = models.TimeField(null=True, blank=True, verbose_name=u'Godzina zamknięcia (Czw)')
	fri_hour_open = models.TimeField(null=True, blank=True, verbose_name=u'Godzina otwarcia (Pią)')
	fri_hour_close = models.TimeField(null=True, blank=True, verbose_name=u'Godzina zamknięcia (Pią)')
	sat_hour_open = models.TimeField(null=True, blank=True, verbose_name=u'Godzina otwarcia (Sob)')
	sat_hour_close = models.TimeField(null=True, blank=True, verbose_name=u'Godzina zamknięcia (Sob)')
	sun_hour_open = models.TimeField(null=True, blank=True, verbose_name=u'Godzina otwarcia (Nie)')
	sun_hour_close = models.TimeField(null=True, blank=True, verbose_name=u'Godzina zamknięcia (Nie)')
	# Koniec godzin otwarcia
	phone = models.CharField(max_length=20, blank=True, null=True, verbose_name=u'Telefon')
	email = models.EmailField(null=True, blank=True, verbose_name=u'Email')
	website = models.URLField(null=True, blank=True, verbose_name=u'Strona www')
	fb = models.URLField(null=True, blank=True, verbose_name=u'Fanpage (FB)')
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
	desc = models.CharField(max_length=150, verbose_name=u'Tekst wyświetlany na stronie głównej', null=True, blank=True, default=None)
	icon = models.CharField(max_length=50, verbose_name=u'Klasa CSS ikony', blank=True, null=True, default=None)
	slug = AutoSlugField(populate_from='name', unique=True, always_update=True, verbose_name=u'Slug')
	home = models.BooleanField(default=False, verbose_name=u'Pokaż na stronie głównej')
	order = models.PositiveSmallIntegerField(default=100, verbose_name=u'Kolejność wyświetlania')

	def __unicode__(self):
		return u'Tag ' + self.name

	class Meta:
		verbose_name = u'Tag'
		verbose_name_plural = u'Tagi'
		ordering = ['order']

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
	desc = models.TextField(null=True, blank=True, default=None, verbose_name=u'Opis')

	def __unicode__(self):
		return u'Zdjęcie lokalu ' + self.place.name

	class Meta:
		verbose_name = u'Zdjęcie lokalu'
		verbose_name_plural = u'Zdjęcia lokalu'

class PlaceMenu(models.Model):
	place = models.ForeignKey('Place', verbose_name=u'Lokal', related_name='menu')
	name = models.CharField(max_length=150, verbose_name='Nazwa pozycji')
	desc = models.TextField(blank=True, null=True, default=None, verbose_name=u'Opis')
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