from django.urls import path
from . import views

app_name='todoapp'

urlpatterns = [
    path('tasks/', views.TaskList.as_view()),
    path('task/<int:pk>', views.TaskDetail.as_view()),
    path('do/<int:pk>', views.markDone),
    path('undo/<int:pk>', views.markUndone),
]
