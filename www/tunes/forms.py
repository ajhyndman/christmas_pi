from django import forms

class PlaySongForm(forms.Form):
    CHOICES = ( (0, 'Christmas Canon'), (1, 'Jingle Bells'), (2, 'Witch Hunt') )
    song = forms.ChoiceField(widget=forms.Select, choices=CHOICES, label='Song:')
