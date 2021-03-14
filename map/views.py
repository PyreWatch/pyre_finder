from django.shortcuts import render
from pyrefinder.settings import env, ENV_DIR
from .models import Fighter

# Create your views here.
def overall_map_view(request):
    mapbox_access_token = str(env("MAPBOX_API_KEY"))


    context = {
        'mapbox_access_token': mapbox_access_token,
        'fighters': Fighter.objects.all()
    }

    return render(request, "mapindex.html", context)