# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PlaceTables'
        db.create_table(u'pnd_placetables', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pnd.Place'])),
            ('table', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('quantity', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'pnd', ['PlaceTables'])

        # Deleting field 'Place.table'
        db.delete_column(u'pnd_place', 'table')

        # Adding field 'Place.places_uid'
        db.add_column(u'pnd_place', 'places_uid',
                      self.gf('django.db.models.fields.TextField')(null=True),
                      keep_default=False)


        # Changing field 'Place.website'
        db.alter_column(u'pnd_place', 'website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'Place.hour_close'
        db.alter_column(u'pnd_place', 'hour_close', self.gf('django.db.models.fields.TimeField')(null=True))

        # Changing field 'Place.phone'
        db.alter_column(u'pnd_place', 'phone', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Changing field 'Place.hour_open'
        db.alter_column(u'pnd_place', 'hour_open', self.gf('django.db.models.fields.TimeField')(null=True))

        # Changing field 'Place.email'
        db.alter_column(u'pnd_place', 'email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True))

        # Changing field 'Place.desc'
        db.alter_column(u'pnd_place', 'desc', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):
        # Deleting model 'PlaceTables'
        db.delete_table(u'pnd_placetables')

        # Adding field 'Place.table'
        db.add_column(u'pnd_place', 'table',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=''),
                      keep_default=False)

        # Deleting field 'Place.places_uid'
        db.delete_column(u'pnd_place', 'places_uid')


        # Changing field 'Place.website'
        db.alter_column(u'pnd_place', 'website', self.gf('django.db.models.fields.URLField')(default='', max_length=200))

        # Changing field 'Place.hour_close'
        db.alter_column(u'pnd_place', 'hour_close', self.gf('django.db.models.fields.TimeField')(default=''))

        # Changing field 'Place.phone'
        db.alter_column(u'pnd_place', 'phone', self.gf('django.db.models.fields.CharField')(default='', max_length=20))

        # Changing field 'Place.hour_open'
        db.alter_column(u'pnd_place', 'hour_open', self.gf('django.db.models.fields.TimeField')(default=''))

        # Changing field 'Place.email'
        db.alter_column(u'pnd_place', 'email', self.gf('django.db.models.fields.EmailField')(default='', max_length=75))

        # Changing field 'Place.desc'
        db.alter_column(u'pnd_place', 'desc', self.gf('django.db.models.fields.TextField')(default=''))

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
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'})
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
        },
        u'pnd.placetables': {
            'Meta': {'object_name': 'PlaceTables'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pnd.Place']"}),
            'quantity': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'table': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        }
    }

    complete_apps = ['pnd']