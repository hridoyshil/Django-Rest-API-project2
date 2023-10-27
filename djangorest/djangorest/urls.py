from django.contrib import admin
from django.urls import path, include
from drapi import views

# from drapi.views import aiquest_create

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("ailist/", views.listModelMixin.as_view(), name="ailist"),
    # path("ailist/<int:pk>", views.listModelMixin.as_view(), name="ailist"),
    path("aicreate/", views.createModelMixin.as_view(), name="aicreate"),
    path("airetrieve/<int:pk>/", views.retrieveModelMixin.as_view(), name="airetrieve"),
    # path("aicreate/", views.AiquestCreate.as_view(), name="aicreate"),
    # path("aicreate/<int:pk>", views.AiquestCreate.as_view(), name="aicreate"),
]
