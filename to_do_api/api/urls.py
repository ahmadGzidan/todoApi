from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ApiOverView.as_view(), name='api-overview'), 
    path('task-list/', views.TaskList.as_view(), name='task-list'),
    path('task-detail/<str:pk>/', views.TaskDetail.as_view(), name='task-detail'),
    path('task-create/', views.TaskCreate.as_view(), name='task-create'),
    path('task-update/<str:pk>/', views.TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<str:pk>/', views.TaskDelete.as_view(), name='task-delete'),
]
