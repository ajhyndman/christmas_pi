from django.shortcuts import render, get_object_or_404
from . import gpio

# Create your views here.
def index(request):
    context = {'switches': gpio.switches}
    return render(request, 'switches/index.html', context)