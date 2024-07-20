from django.urls import path
from pages.views import HomeView, AboutPageview

urlpatterns = [
    path("electronica",HomeView.as_view(),name= "home"),
    path("about/", AboutPageview.as_view(), name= "about"),
]
