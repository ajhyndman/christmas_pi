from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render
from django.core.urlresolvers import reverse


# Create your views here.
def index(request):
    context = {'nav_links': [
        {
            'label': 'Switches',
            'url': reverse('switches:index', args=()),
        },
        {
            'label': 'Tunes',
            'url': reverse('tunes:index', args=()),
        },
    ]}
    return render(request, 'index.html', context)