from django.conf.urls import url

from . import views

app_name = 'tunes'
urlpatterns = [
    # ex: /tunes/
    url(r'^$', views.index, name='index'),
    # ex: /tunes/5/play/
    url(r'^(?P<pk>[0-9]+)/play/$', views.play, name='play'),
    # ex: POST /tuns/playmusic/ with a form for song index
    url(r'^playmusic/$', views.playmusic, name='playmusic'),
    # ex /tunes/stopmusic/
    url(r'^stopmusic/$', views.stopmusic, name='stopmusic'),
]
