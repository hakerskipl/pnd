# Create your views here.
from django.shortcuts import render_to_response
from pnd.models import *

def index(request):
	return render_to_response('index.html', context_instance=RequestContext(request))

def results(request):
	return render_to_response('wyniki.html', context_instance=RequestContext(request))

def detail(request):
	return render_to_response('detail.html', context_instance=RequestContext(request))