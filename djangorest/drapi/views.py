# from rest_framework.views import APIView
# from rest_framework.response import Response

from django.shortcuts import render
from .serializers import Aiquestserializer
from .models import Aiquest
from rest_framework import mixins
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class Aiquest_list_Create(ListCreateAPIView):
    queryset = Aiquest.objects.all()
    serializer_class = Aiquestserializer


class Aiquest_Retrieve_Update_Destroy(RetrieveUpdateDestroyAPIView):
    queryset = Aiquest.objects.all()
    serializer_class = Aiquestserializer


# class AiquestCreate(APIView):
#     def get(self, request, pk=None, format=None):
#         id = pk
#         if id is not None:
#             # comples data
#             ai = Aiquest.objects.get(id=id)
#             # python dect
#             serializer = Aiquestserializer(ai)
#             return Response(serializer.data)

#         # complex data
#         ai = Aiquest.objects.all()
#         # python dect
#         serializer = Aiquestserializer(ai, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = Aiquestserializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg": "Successfully insert data!"})
#         return Response(serializer.errors)

#     def put(self, request, pk, format=None):
#         id = pk
#         ai = Aiquest.objects.get(pk=id)
#         # python dect
#         serializer = Aiquestserializer(ai, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg": "Successfully full data update!"})
#         return Response(serializer.errors)

#     def patch(self, request, pk=None, format=None):
#         id = pk
#         ai = Aiquest.objects.get(pk=id)
#         # python dect
#         serializer = Aiquestserializer(ai, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg": "partial data update !"})
#         return Response(serializer.errors)

#     def delete(self, request, pk=None, format=None):
#         id = pk
#         ai = Aiquest.objects.get(pk=id)
#         ai.delete()
#         return Response({"msg": "Successfully delete update !"})
