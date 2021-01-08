from django.urls import path
from . import views
app_name = 'multiplerelationexample'

urlpatterns = [
    path('create/', views.CreateMeal.as_view()),
]