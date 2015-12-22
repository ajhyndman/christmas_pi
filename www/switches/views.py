from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from . import gpio


# Create your views here.
def index(request):
    context = {'switch_status': [sw.get_status() for sw in gpio.SWITCHES]}
    return render(request, 'switches/index.html', context)    
    
def toggle(request, pk):
    switch = gpio.SWITCHES[int(pk)-1]
    switch.toggle()
    return HttpResponseRedirect(reverse('switches:index', args=()))