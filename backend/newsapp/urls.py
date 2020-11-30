from django.urls import path
from . import views

app_name = 'newsapp'

urlpatterns = [
        path('articles/', views.NewsArticleList.as_view()),
        path('article/<int:pk>', views.NewsArticleDetail.as_view()),
]
