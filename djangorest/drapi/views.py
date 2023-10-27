from django.shortcuts import render
from .serializers import Aiquestserializer
from .models import Aiquest
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET", "POST", "PUT", "PATCH", "DELETE"])
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

    if request.method == "POST":
        serializer = Aiquestserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Successfully insert data!"})
        return Response(serializer.errors)

    if request.method == "PUT":
        id = pk
        ai = Aiquest.objects.get(pk=id)
        # python dect
        serializer = Aiquestserializer(ai, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Successfully full data update!"})
        return Response(serializer.errors)

    if request.method == "PATCH":
        id = pk
        ai = Aiquest.objects.get(pk=id)
        # python dect
        serializer = Aiquestserializer(ai, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "partial data update !"})
        return Response(serializer.errors)

    if request.method == "DELETE":
        id = pk
        ai = Aiquest.objects.get(pk=id)
        ai.delete()
        return Response({"msg": "Successfully delete update !"})
