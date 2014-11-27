# -*- coding: utf-8 -*-

from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string

