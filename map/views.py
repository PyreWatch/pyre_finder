from django.shortcuts import render
from pyrefinder.settings import env, ENV_DIR

# Create your views here.
def overall_map_view(request):
    mapbox_access_token = str(env("MAPBOX_API_KEY"))
    return render(request, "mapindex.html", {'mapbox_access_token': mapbox_access_token })