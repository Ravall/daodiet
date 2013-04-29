# -*- coding: utf-8 -*-
from django import template
register = template.Library()
from datetime import timedelta

def strfdelta(tdelta, fmt):
    d = {"days": tdelta.days}
    d["hours"], rem = divmod(tdelta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    d["sign"] = '+' if tdelta > timedelta(seconds=1) else '-'
    return fmt.format(**d)

@register.filter
def suntime_diff(dimedelta):
    return strfdelta(dimedelta, "{sign}{hours}:{minutes}")

