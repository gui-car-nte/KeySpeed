from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit_test/', views.submit_test, name='submit_test'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'), #type: ignore
]
