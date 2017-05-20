# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
	return HttpResponse(u"欢迎自学!!")

def add(request):
	a = request.GET['a']
	b = request.GET['b']
	# c = int(a) + int(b)
	# return HttpResponse(str(c))
	return HttpResponseRedirect(
			reverse('add2', args={a, b})
		)

def add2(request, a, b):
	c = int(a) + int(b)
	return HttpResponse(str(c))

def home(request):
	items = [u'张三', u'李四', u'王五']
	return render(request, 'learn/home.html', {'string':u'张三', 'items':items })