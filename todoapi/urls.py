from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authapp.urls')), # for registration and login
    path('api/', include('tasks.urls')),  # for tasks
]
