from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('update/<pk>', views.update_task, name='update_task'),
    path('delete/<pk>', views.delete_task, name='delete_task'),
]