from django.conf.urls import url

from . import views

app_name = 'switches'
urlpatterns = [
    # ex: /switches/
    url(r'^$', views.index, name='index'),
    # ex: /switches/5/toggle/
    url(r'^(?P<pk>[0-9]+)/toggle/$', views.toggle, name='toggle'),
]