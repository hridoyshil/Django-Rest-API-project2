from django.contrib import admin
from django.urls import path, include
from drapi import views

# from drapi.views import aiquest_create

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("aicreate/", views.aiquest_create, name="aicreate"),
    path("aicreate/<int:pk>", views.aiquest_create, name="aicreate"),
]
