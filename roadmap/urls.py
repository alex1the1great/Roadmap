from django.urls import path

from . import views

urlpatterns = [
    path('', views.goal_list, name='goal_list'),
    path('/add/', views.goal_add, name='goal_add')
]
