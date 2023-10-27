from django.contrib import admin
from django.urls import path, include
from drapi import views

# from drapi.views import aiquest_create

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("ailistcreate/", views.Aiquest_list_Create.as_view(), name="ailist"),
    path(
        "airetrieve/<int:pk>/",
        views.Aiquest_Retrieve_Update_Destroy.as_view(),
        name="airetrieve",
    ),
]
