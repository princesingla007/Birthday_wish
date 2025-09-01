
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("puzzel",views.puzzel,name="puzzel"),
    path("cake_cut",views.cake_cut,name="cake_cut"),
    path("surprise_box",views.surprise_box,name="surprise_box"),
    path("balloon",views.balloon,name="balloon"),
    path("last",views.last,name="last"),
]

