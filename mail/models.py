# -*- coding: utf-8 -*-
from django.db import models
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from forward.settings import ADMIN_EMAIL


# Create your models here.
class PromoMail(models.Model):
    name = models.CharField(verbose_name=u'Заголовок письма', max_length=100)
    sender = models.EmailField(verbose_name=u'E-mail отправителя', max_length=100)
    recipient = models.EmailField(verbose_name=u'Е-mail получателя', max_length=100)
    subject = models.CharField(verbose_name=u'Тема письма', max_length=100)
    template = models.CharField(verbose_name=u'Шаблон для письма (например: mail/promoforward.html)', max_length=100 )

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Комерческое предложение'
        verbose_name_plural = u'Отпарвка комерческих предложений'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):

        context_dict = {
                'title': self.name,
            }

        message = render_to_string('%s' % self.template, context_dict)
        msg = EmailMultiAlternatives(self.subject, message, ADMIN_EMAIL, [self.recipient])
        msg.content_subtype = "html"
        msg.send()

        return super(PromoMail, self).save(force_insert, force_update, using)