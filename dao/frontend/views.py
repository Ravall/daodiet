# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from frontend.models import MyCity


def index(request):
    #request.META['REMOTE_ADDR'] = '109.74.128.94'
    city = MyCity('86.45.76.211')

    return render_to_response(
        'frontend/index.html',
        {'city': city},
        context_instance=RequestContext(request)
    )