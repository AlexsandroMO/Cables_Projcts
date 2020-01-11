
from django.urls import path
from . import views

urlpatterns = [
    path('homecalc', views.homecalc, name='home-calc'),
    #path('tasklist/<int:id>', views.taskList, name='task-list'),
    #path('newtask/', views.newTask, name='new-task'),
    #path('edittask/<int:id>', views.editTask, name='edit-task'),
    #path('deletetask/<int:id>', views.deleteTask, name='delete-task'),


]