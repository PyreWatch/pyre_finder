from django.shortcuts import render

# Create your views here.
def overall_map_view(request):
    return render(request, "mapindex.html")