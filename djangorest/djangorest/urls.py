from django.contrib import admin
from django.urls import path, include
from drapi import views
from rest_framework.routers import DefaultRouter

# create router object
router = DefaultRouter()
# router register
router.register("viewsets", views.Aiquest_Model_ViewSet, basename="hridoy")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("", include(router.urls)),
]
