# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'BlogPost.author_choice'
        db.alter_column(u'blog_blogpost', 'author_choice', self.gf('django.db.models.fields.CharField')(max_length=8))

    def backwards(self, orm):

        # Changing field 'BlogPost.author_choice'
        db.alter_column(u'blog_blogpost', 'author_choice', self.gf('django.db.models.fields.CharField')(max_length=7))

    models = {
        u'blog.blogpost': {
            'Meta': {'object_name': 'BlogPost'},
            'author_choice': ('django.db.models.fields.CharField', [], {'default': "'korovkin'", 'max_length': '8'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'default': "'default'", 'unique_with': '()', 'max_length': '50', 'populate_from': 'None'}),
            'text': ('ckeditor.fields.RichTextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title_tag': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'blog.post': {
            'Meta': {'object_name': 'Post'},
            'blue_choice': ('django.db.models.fields.CharField', [], {'default': "'notblue'", 'max_length': '7'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'image_blue': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'main_choice': ('django.db.models.fields.CharField', [], {'default': "'notmain'", 'max_length': '7'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'default': "'default'", 'unique_with': '()', 'max_length': '50', 'populate_from': 'None'}),
            'text': ('ckeditor.fields.RichTextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['blog']