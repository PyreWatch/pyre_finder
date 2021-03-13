from django.urls import path

from . import views

urlpatterns = [
    path('', views.overall_map_view, name='overall_map_view'),
]