from django.urls import path

from . import views

urlpatterns = [
    path('hospitals/<int:hospitalId>/appointmentSlots/', views.index, name='index'),
]