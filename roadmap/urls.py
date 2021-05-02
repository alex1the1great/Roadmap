from django.urls import path

from . import views

urlpatterns = [
    path('', views.goal_list, name='goal_list'),
    path('add/', views.goal_add, name='goal_add'),
    path('<slug:slug>/edit/', views.goal_edit, name='goal_edit'),
    path('<slug:slug>/delete/', views.goal_delete, name='goal_delete')
]
