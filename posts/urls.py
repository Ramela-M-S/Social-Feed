from django.urls import path
from . import views

urlpatterns = [
    path('all_posts/', views.all_posts, name='all_posts'),
    path('my_posts/', views.my_posts, name='my_posts'),
    path('create/', views.create_view, name = "create"),
    path('menu/', views.menu_view, name = "menu")
]