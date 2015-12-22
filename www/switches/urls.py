from django.conf.urls import url

from . import views

app_name = 'switches'
urlpatterns = [
    # ex: /switches/
    url(r'^$', views.index, name='index'),
]