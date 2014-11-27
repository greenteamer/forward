# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PromoMail.sender'
        db.add_column(u'mail_promomail', 'sender',
                      self.gf('django.db.models.fields.EmailField')(default='teamer777@gmail.com', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'PromoMail.sender'
        db.delete_column(u'mail_promomail', 'sender')


    models = {
        u'mail.promomail': {
            'Meta': {'object_name': 'PromoMail'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'recipient': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'sender': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'template': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['mail']