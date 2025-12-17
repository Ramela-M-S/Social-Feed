from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', views.home_view, name = "home")
]