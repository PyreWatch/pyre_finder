from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from pyrefinder.settings import env, ENV_DIR

# Create your views here.
@login_required(login_url='accounts/login')
def index(request):
    mapbox_access_token = str(env("MAPBOX_API_KEY"))
    return render(request, "map/index.html", {'mapbox_access_token': mapbox_access_token })