from django.urls import path
from . import views
app_name = 'multiplerelationexample'

urlpatterns = [
    path('create/meal/', views.CreateMeal.as_view()),
]