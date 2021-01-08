from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('newsapp.urls')),
    path('todo/', include('todoapp.urls')),
    path('menu/', include('restaurant_menu.urls')),
    path('multi/', include('multirelationexample.urls')),
]
