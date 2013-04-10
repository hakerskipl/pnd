# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Place'
        db.create_table(u'pnd_place', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=50, populate_from='name', unique_with=())),
            ('short', self.gf('django.db.models.fields.TextField')(null=True)),
            ('desc', self.gf('django.db.models.fields.TextField')(null=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('hour_open', self.gf('django.db.models.fields.TimeField')(null=True)),
            ('hour_close', self.gf('django.db.models.fields.TimeField')(null=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
            ('places_uid', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal(u'pnd', ['Place'])

        # Adding M2M table for field tags on 'Place'
        db.create_table(u'pnd_place_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('place', models.ForeignKey(orm[u'pnd.place'], null=False)),
            ('tags', models.ForeignKey(orm[u'pnd.tags'], null=False))
        ))
        db.create_unique(u'pnd_place_tags', ['place_id', 'tags_id'])

        # Adding model 'Tags'
        db.create_table(u'pnd_tags', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('icon', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'pnd', ['Tags'])

        # Adding model 'PlaceTables'
        db.create_table(u'pnd_placetables', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tables', to=orm['pnd.Place'])),
            ('table', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('quantity', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'pnd', ['PlaceTables'])

        # Adding model 'PlacePhotos'
        db.create_table(u'pnd_placephotos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(related_name='photos', to=orm['pnd.Place'])),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('photo_thumbnail', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100)),
            ('desc', self.gf('django.db.models.fields.TextField')(default=None, null=True)),
        ))
        db.send_create_signal(u'pnd', ['PlacePhotos'])

        # Adding model 'PlaceMenu'
        db.create_table(u'pnd_placemenu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(related_name='menu', to=orm['pnd.Place'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('desc', self.gf('django.db.models.fields.TextField')()),
            ('price', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=5, decimal_places=2)),
        ))
        db.send_create_signal(u'pnd', ['PlaceMenu'])

        # Adding model 'TodaysIdea'
        db.create_table(u'pnd_todaysidea', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pomysly', to=orm['pnd.Place'])),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 4, 10, 0, 0))),
            ('slogan', self.gf('django.db.models.fields.CharField')(default=None, max_length=150, null=True)),
            ('photo', self.gf('imagekit.models.fields.ProcessedImageField')(default=None, max_length=100, null=True)),
        ))
        db.send_create_signal(u'pnd', ['TodaysIdea'])


    def backwards(self, orm):
        # Deleting model 'Place'
        db.delete_table(u'pnd_place')

        # Removing M2M table for field tags on 'Place'
        db.delete_table('pnd_place_tags')

        # Deleting model 'Tags'
        db.delete_table(u'pnd_tags')

        # Deleting model 'PlaceTables'
        db.delete_table(u'pnd_placetables')

        # Deleting model 'PlacePhotos'
        db.delete_table(u'pnd_placephotos')

        # Deleting model 'PlaceMenu'
        db.delete_table(u'pnd_placemenu')

        # Deleting model 'TodaysIdea'
        db.delete_table(u'pnd_todaysidea')


    models = {
        u'pnd.place': {
            'Meta': {'ordering': "['name']", 'object_name': 'Place'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'desc': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'}),
            'hour_close': ('django.db.models.fields.TimeField', [], {'null': 'True'}),
            'hour_open': ('django.db.models.fields.TimeField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'places_uid': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'short': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'name'", 'unique_with': '()'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['pnd.Tags']", 'symmetrical': 'False'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'})
        },
        u'pnd.placemenu': {
            'Meta': {'ordering': "['place', 'name']", 'object_name': 'PlaceMenu'},
            'desc': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'menu'", 'to': u"orm['pnd.Place']"}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '5', 'decimal_places': '2'})
        },
        u'pnd.placephotos': {
            'Meta': {'object_name': 'PlacePhotos'},
            'desc': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'photo_thumbnail': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photos'", 'to': u"orm['pnd.Place']"})
        },
        u'pnd.placetables': {
            'Meta': {'object_name': 'PlaceTables'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tables'", 'to': u"orm['pnd.Place']"}),
            'quantity': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'table': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        u'pnd.tags': {
            'Meta': {'ordering': "['name']", 'object_name': 'Tags'},
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'pnd.todaysidea': {
            'Meta': {'ordering': "['-date']", 'object_name': 'TodaysIdea'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 4, 10, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('imagekit.models.fields.ProcessedImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pomysly'", 'to': u"orm['pnd.Place']"}),
            'slogan': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '150', 'null': 'True'})
        }
    }

    complete_apps = ['pnd']