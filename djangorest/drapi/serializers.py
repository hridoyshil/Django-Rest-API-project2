from rest_framework import serializers
from .models import Aiquest


class Aiquestserializer(serializers.ModelSerializer):
    class Meta:
        model = Aiquest
        fields = ["teacher_name", "course_name", "course_duration", "seat"]
