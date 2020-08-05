from todo_app import views
from django.urls import path
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('tasks/', views.tasks_todo, name='task_list'),
    path('tasks/add_todo/', views.add_todo, name='add_todo'),
    path('tasks/<int:id>/delete_task/', views.delete_task, name='delete_task'),
    path('tasks/<int:id>/', views.detail_task, name='detail_task'),
    path('tasks/<int:id>/update_task/', views.update_task, name='update_task'),
]