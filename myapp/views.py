from django.shortcuts import render
from django.http import JsonResponse
from .models import *

# Create your views here.
def index(request):

    return render(request, 'index.html')

def get_data(request):
    latest_Data = LocationUpdate.objects.latest('timestamp')
    return JsonResponse({
        'latitude': latest_Data.latitude,
        'longitude' : latest_Data.longitude,
        'timestamp': latest_Data.timestamp
    })