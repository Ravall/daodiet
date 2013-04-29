# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from frontend.models import MyCity


def index(request):
    #city = MyCity('86.45.76.211')
    #city = MyCity('37.113.183.57')
    city = MyCity(request.META['REMOTE_ADDR'])

    return render_to_response(
        'frontend/index.html',
        {'city': city},
        context_instance=RequestContext(request)
    )