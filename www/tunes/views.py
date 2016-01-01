from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render
from django.core.urlresolvers import reverse
import score
import tunes
import musicplayer
import forms

def index(request):
    context = {
        'tunes': [tune for tune in tunes.TUNES],
        'form': forms.PlaySongForm(),
        # 'is_playing': musicplayer.PLAYER.is_playing(),
    }
    return render(request, 'tunes/index.html', context)

def play(request, pk = 0):
    tune = tunes.TUNES[int(pk)-1]
    tune.play()
    return HttpResponseRedirect(reverse('tunes:index', args=()))

def playmusic(request):
    song_index = 0
    if request.method == 'POST':
        form = forms.PlaySongForm(request.POST)
        if form.is_valid():
            song_index = int(form.cleaned_data['song'])
    musicplayer.PLAYER.play(int(song_index))
    return HttpResponseRedirect(reverse('tunes:index', args=()))

def stopmusic(request):
    musicplayer.PLAYER.stop()
    return HttpResponseRedirect(reverse('tunes:index', args=()))
