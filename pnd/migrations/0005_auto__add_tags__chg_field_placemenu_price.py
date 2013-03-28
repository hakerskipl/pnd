# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tags'
        db.create_table(u'pnd_tags', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'pnd', ['Tags'])

        # Adding M2M table for field tags on 'Place'
        db.create_table(u'pnd_place_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('place', models.ForeignKey(orm[u'pnd.place'], null=False)),
            ('tags', models.ForeignKey(orm[u'pnd.tags'], null=False))
        ))
        db.create_unique(u'pnd_place_tags', ['place_id', 'tags_id'])


        # Changing field 'PlaceMenu.price'
        db.alter_column(u'pnd_placemenu', 'price', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2))

    def backwards(self, orm):
        # Deleting model 'Tags'
        db.delete_table(u'pnd_tags')

        # Removing M2M table for field tags on 'Place'
        db.delete_table('pnd_place_tags')


        # Changing field 'PlaceMenu.price'
        db.alter_column(u'pnd_placemenu', 'price', self.gf('django.db.models.fields.CharField')(max_length=10))

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
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['pnd.Tags']", 'symmetrical': 'False'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'})
        },
        u'pnd.placemenu': {
            'Meta': {'ordering': "['place', 'name']", 'object_name': 'PlaceMenu'},
            'desc': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pnd.Place']"}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '5', 'decimal_places': '2'})
        },
        u'pnd.placephotos': {
            'Meta': {'object_name': 'PlacePhotos'},
            'desc': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pnd.Place']"})
        },
        u'pnd.placetables': {
            'Meta': {'object_name': 'PlaceTables'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stoliki'", 'to': u"orm['pnd.Place']"}),
            'quantity': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'table': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        u'pnd.tags': {
            'Meta': {'ordering': "['name']", 'object_name': 'Tags'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['pnd']