from django.urls import path

from . import views

urlpatterns = [
    path('', views.goal_list, name='goal_list'),
    path('add/', views.goal_add, name='goal_add'),
    path('<slug:slug>/detail/', views.goal_detail, name='goal_detail'),
    path('<slug:slug>/edit/', views.goal_edit, name='goal_edit'),
    path('<slug:slug>/delete/', views.goal_delete, name='goal_delete'),

    path('<slug:slug>/task/add/', views.task_add, name='task_add'),
    path('task/<int:task_id>/', views.task_delete, name='task_delete')
]
