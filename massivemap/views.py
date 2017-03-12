from django.shortcuts import render

# Create your views here.
def map_start(request):
    return render(request, 'map/map_start.html')

def map_test(request):
    return render(request, 'map/map_test.html')

def map_plain(request):
    return render(request, 'map/map_plain.html')

def map_fancy(request):

    return render(request, 'map/map_fancy.html')