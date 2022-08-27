from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.measurements_view, name='measurements_view'),  # type: ignore
    path('<int:pk>', views.measurement_view, name='measurement_view'),  # type: ignore
]