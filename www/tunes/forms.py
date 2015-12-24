from django import forms
import musicplayer

class PlaySongForm(forms.Form):
    CHOICES = musicplayer.PLAYER.song_list()
    song = forms.ChoiceField(widget=forms.Select, choices=CHOICES, label='Song:')
