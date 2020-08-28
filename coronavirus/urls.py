from django.urls import path
from . import views

urlpatterns = [
	path('country_view/<int:id>/', views.country_view, name="country_view"),
	path('', views.home, name="home"),
]