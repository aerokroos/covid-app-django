from django.urls import path
from . import views

urlpatterns = [
	path('country_view/', views.ViewCountryData.as_view(), name="country_view"),
	path('', views.home, name="home"),
]