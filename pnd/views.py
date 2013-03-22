#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from pnd.models import *

def index(request):
	return render_to_response('index.html', context_instance=RequestContext(request))

def results(request):
	return render_to_response('wyniki.html', context_instance=RequestContext(request))

def detail(request):
	return render_to_response('detail.html', context_instance=RequestContext(request))