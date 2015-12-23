from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render
from django.core.urlresolvers import reverse
from . import score
from . import tunes
from subprocess import call

# Create your views here.
def index(request):
    context = {'tunes': [tune.name for tune in tunes.TUNES]}
    return render(request, 'tunes/index.html', context)

def play(request, pk):
    tune = tunes.TUNES[int(pk)-1]
    tune.play()
    return HttpResponseRedirect(reverse('tunes:index', args=()))

def playmusic(request):
    call(["omxplayer", "/home/pi/christmas_pi/songs/Witch Hunt.mp3"])
    return HttpResponseRedirect(reverse('tunes:index', args=()))
