# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import trans
import ephem
import pytz
from ipgeo.models import Range
from pygeoip import GeoIP
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ungettext
from django.contrib.staticfiles.storage import staticfiles_storage
from datetime import datetime, date, time


class MyCity:

    def translite(self, string):
        '''
        транслитерация. подходит для seo
        '''
        def eu8(string):
            return string.encode('utf-8')
        return eu8(unicode(string.replace(' ', '_')).encode('trans').lower())

    def _get_city_image(self, city):
        """
        определение изображения города
        """
        city_tr = self.translite(city)
        if staticfiles_storage.exists(
            settings.STATIC_ROOT + '/images/city/{0}.jpg'.format(city_tr)
        ):
            city_img = city_tr
        else:
            city_img = 'default'
        return city_img

    def set_location(self, **kwargs):
        self.city = kwargs['city']
        self.longitude = kwargs['longitude']
        self.latitude = kwargs['latitude']
        self.timezone = kwargs['timezone']
        self.city_img = self._get_city_image(self.city)
        self.sunrise, self.sunset = self.get_sun_positions(
            self.longitude, self.latitude, self.timezone
        )
        self.zenit = (self.sunrise + (self.sunset - self.sunrise)/2)
        print self.sunset, self.sunrise
        #print datetime.combine(date.today(), time(12,0))
        self.diff = self.zenit - datetime.combine(date.today(), time(12, 0))

    @staticmethod
    def get_sun_positions(longitude, latitude, timezone):
        observ = ephem.Observer()
        observ.lat = str(latitude)
        observ.long = str(longitude)
        sun_observ = ephem.Sun()
        sun_observ.compute()

        sunrise = (observ.previous_rising(sun_observ)).datetime()
        # если текущее время до восхода солнца, то фунция previous_rising
        # вернет предыдущий день, а нужно сегодняшний
        if sunrise < datetime.combine(date.today(), time(0, 1)):
            sunrise = (observ.next_rising(sun_observ)).datetime()

        sunset = (observ.next_setting(sun_observ)).datetime()
        # если текущее время после захода солнца, то фунция next_setting
        # вернет заход солнца на следующий день, а нужно на сегодняшний
        if sunset > datetime.combine(date.today(), time(23, 59)):
            sunset = observ.previous_setting(sun_observ).datetime()

        tz = pytz.timezone(timezone)
        sunset = sunset + tz.utcoffset(sunset)
        sunrise = sunrise + tz.utcoffset(sunrise)
        return (sunrise, sunset)

    def __init__(self, ip):
        class CityNotDetected(Exception):
            pass
        try:
            # если не удалось определить через ipgeo
            # то определяем через pygeoip
            geo = GeoIP(settings.GEO_CITY_DAT_FILE)
            location = geo.record_by_addr(ip)
            if not location:
                raise CityNotDetected(
                    'не удалось определить через pygeoip'
                )
            city_name = location['city']
            longitude = location['longitude']
            latitude = location['latitude']
            if location['country_name'] == 'Russian Federation':
                try:
                    # определяем положение через ipgeo
                    geo = Range.objects.find(ip)
                    if not geo.location:
                        raise CityNotDetected(
                            'Не удалось определить через ipgeo'
                        )
                    city_name = geo.location.name
                    longitude = geo.location.lon
                    latitude = geo.location.lat
                except (CityNotDetected, Range.DoesNotExist):
                    pass
            self.set_location(
                city=city_name,
                longitude=longitude,
                latitude=latitude,
                timezone=location['time_zone']
            )
        except CityNotDetected:
            # если ничего не определили - считаем что позиция мск
            self.set_location(
                city='Москва',
                longitude=settings.MSK_LONGITUDE,
                latitude=settings.MSK_LATITUDE,
                timezone='Europe/Moscow'
            )
