from django.urls import path
from . import views  # or import views from other apps if necessary

urlpatterns = [
    path('', views.index, name='index'),
    # Add other URLs as needed
]