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
            ('desc', self.gf('django.db.models.fields.TextField')()),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('hour_open', self.gf('django.db.models.fields.TimeField')()),
            ('hour_close', self.gf('django.db.models.fields.TimeField')()),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('table', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'pnd', ['Place'])

        # Adding model 'PlaceMenu'
        db.create_table(u'pnd_placemenu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pnd.Place'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('desc', self.gf('django.db.models.fields.TextField')()),
            ('price', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'pnd', ['PlaceMenu'])

        # Adding model 'PlacePhotos'
        db.create_table(u'pnd_placephotos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pnd.Place'])),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('desc', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'pnd', ['PlacePhotos'])


    def backwards(self, orm):
        # Deleting model 'Place'
        db.delete_table(u'pnd_place')

        # Deleting model 'PlaceMenu'
        db.delete_table(u'pnd_placemenu')

        # Deleting model 'PlacePhotos'
        db.delete_table(u'pnd_placephotos')


    models = {
        u'pnd.place': {
            'Meta': {'ordering': "['name']", 'object_name': 'Place'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'desc': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'hour_close': ('django.db.models.fields.TimeField', [], {}),
            'hour_open': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'table': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'pnd.placemenu': {
            'Meta': {'ordering': "['place', 'name']", 'object_name': 'PlaceMenu'},
            'desc': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pnd.Place']"}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'pnd.placephotos': {
            'Meta': {'object_name': 'PlacePhotos'},
            'desc': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pnd.Place']"})
        }
    }

    complete_apps = ['pnd']