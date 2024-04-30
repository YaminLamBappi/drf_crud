from django.urls import path
from . import views

urlpatterns = [
    path('', views.family_list, name='family_list'),
    path('add/', views.add_family, name='add_family'),
    path('familyapi/', views.FamilyApi.as_view())
]
