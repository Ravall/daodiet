from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from ipgeo.models import Range
from pygeoip import GeoIP
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class MyCity:

    def set_location(self, **kwargs):
        self.city = kwargs['city']
        self.longitude = kwargs['longitude']
        self.latitude = kwargs['latitude']


    def __init__(self, ip):
        try:
            geo = Range.objects.find(ip)
            if not geo.location:
                raise Range.DoesNotExist
        except Range.DoesNotExist:
            geo = GeoIP(settings.GEO_CITY_DAT_FILE)
            location = geo.record_by_addr(ip)
            self.set_location(
                city=_(location['city']),
                longitude=location['longitude'],
                latitude=location['latitude']
            )

