from django.shortcuts import render
from .serializers import Aiquestserializer
from .models import Aiquest
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def aiquest_create(request, pk=None):
    if request.method == "GET":
        id = pk
        if id is not None:
            # comples data
            ai = Aiquest.objects.get(id=id)
            # python dect
            serializer = Aiquestserializer(ai)
            return Response(serializer.data)

        # complex data
        ai = Aiquest.objects.all()
        # python dect
        serializer = Aiquestserializer(ai, many=True)
        return Response(serializer.data)
