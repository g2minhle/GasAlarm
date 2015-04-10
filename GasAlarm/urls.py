from django.conf.urls import patterns, include, url
from django.contrib import admin
from GasAlarm.actions import setPhoneNumber

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'GasAlarm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^setPhoneNumber/', setPhoneNumber),
)
