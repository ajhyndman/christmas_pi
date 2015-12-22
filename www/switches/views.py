from django.shortcuts import render
from . import gpio

# Create your views here.
def index(request):
    
    context = {
        'switch_one'   : gpio.switch_one,
        'switch_two'   : gpio.switch_two,
        'switch_three' : gpio.switch_three,
        'switch_four'  : gpio.switch_four,
    }
    return render(request, 'switches/index.html', context)