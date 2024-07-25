from django.urls import path
from . import views

urlpatterns = [
    path('', views.global_ranking, name='ranking'),
    path('personal/', views.personal_ranking, name='personal_ranking'),
]
