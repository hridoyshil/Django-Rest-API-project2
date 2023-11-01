from django.shortcuts import render
from .serializers import Aiquestserializer
from .models import Aiquest
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser


class Aiquest_Model_ViewSet(viewsets.ModelViewSet):
    # List, Create, delete, update, partinal, patch
    queryset = Aiquest.objects.all()
    serializer_class = Aiquestserializer
    permission_classes = [IsAdminUser]
