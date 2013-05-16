# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from frontend.models import MyCity
from django.conf import settings


def index(request):
    #city = MyCity('86.45.76.211')
    #city = MyCity('37.113.183.57')
    city = MyCity(request.META['REMOTE_ADDR'])

    return render_to_response(
        'frontend/index.html',
        {
            'city': city,
            'time': {
                'wake_up': settings.WAKEUP_TIME,
                'breakfast': settings.BREAKFAST_TIME,
                'lunch': settings.LUNCH_TIME,
                'dinner': settings.DINNER_TIME,
                'sleep': settings.SLEEP_TIME
            }
        },
        context_instance=RequestContext(request)
    )

def page(request):
    city = MyCity(request.META['REMOTE_ADDR'])

    return render_to_response(
        'frontend/page.html',
        {
            'city': city,
            'time': {
                'noon': settings.WAKEUP_NOON,
            }
        },
        context_instance=RequestContext(request)
    )


