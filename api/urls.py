from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.ApiOverview, name='api-overview'),
    path('task-list/', views.TaskList.as_view(), name='task-list'),
    path('task-create/', views.TaskList.as_view(), name='task-create'),
    path('task-detail/<str:pk>/', views.TaskDetail.as_view(), name='task-detail'),
    path('task-update/<str:pk>/', views.update_task, name='task-update'),
    path('task-delete/<str:pk>/', views.TaskDetail.as_view(), name='task-delete'),
]
