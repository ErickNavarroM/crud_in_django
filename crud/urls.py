"""
URL configuration for crud_in_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from crud import views

urlpatterns = [
    path('create_task', views.CreateTaskView.as_view(), name="create_task"),
    path('', views.ReadTaskView.as_view(), name="read_tasks"),
    path('update_task/<int:id>', views.UpdateTaskView.as_view(), name="update_task"),
    path('delete_task/<int:id>', views.DeleteTaskView.as_view(), name="delete_task"),
]
