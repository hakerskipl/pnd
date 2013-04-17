# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'PlaceMenu.desc'
        db.alter_column(u'pnd_placemenu', 'desc', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):

        # Changing field 'PlaceMenu.desc'
        db.alter_column(u'pnd_placemenu', 'desc', self.gf('django.db.models.fields.TextField')(default=''))

    models = {
        u'pnd.place': {
            'Meta': {'ordering': "['name']", 'object_name': 'Place'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'hour_close': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'hour_open': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'places_uid': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'short': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'name'", 'unique_with': '()'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['pnd.Tags']", 'symmetrical': 'False'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'pnd.placemenu': {
            'Meta': {'ordering': "['place', 'name']", 'object_name': 'PlaceMenu'},
            'desc': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'menu'", 'to': u"orm['pnd.Place']"}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '5', 'decimal_places': '2'})
        },
        u'pnd.placephotos': {
            'Meta': {'object_name': 'PlacePhotos'},
            'desc': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
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
            'Meta': {'ordering': "['order']", 'object_name': 'Tags'},
            'desc': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'home': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'icon': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '100'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'name'", 'unique_with': '()'})
        },
        u'pnd.todaysidea': {
            'Meta': {'ordering': "['-date']", 'object_name': 'TodaysIdea'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 4, 16, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('imagekit.models.fields.ProcessedImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pomysly'", 'to': u"orm['pnd.Place']"}),
            'slogan': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '150', 'null': 'True'})
        }
    }

    complete_apps = ['pnd']