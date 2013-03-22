# Create your views here.
from django.shortcuts import render_to_response
from pnd.models import *

def index(request):
	return render_to_response('index.html')

def results(request):
	return render_to_response('wyniki.html')

def detail(request):
	return render_to_response('detail.html')