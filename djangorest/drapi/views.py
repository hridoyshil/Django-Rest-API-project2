from django.shortcuts import render
from .serializers import Aiquestserializer
from .models import Aiquest
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser

# Create your views here.


# Queryset
def aiquest_info(request):
    # complex data
    ai = Aiquest.objects.all()
    # python dict/native python data
    serializer = Aiquestserializer(ai, many=True)
    # render json
    json_data = JSONRenderer().render(serializer.data)
    # json sent to user/display/Front-End
    return HttpResponse(json_data, content_type="application/json")


# model instance
def aiquest_ins(request, pk):
    # complex data
    ai = Aiquest.objects.get(id=pk)
    # python dict/native python data
    serializer = Aiquestserializer(ai)
    # render json
    json_data = JSONRenderer().render(data=serializer.data)
    # json sent to user/display/Front-End
    return HttpResponse(json_data, content_type="application/json")


@csrf_exempt
def aiquest_create(request):
    if request.method == "POST":
        json_data = request.body
        # json to stream convert
        stream = io.BytesIO(json_data)
        # stream to python convert
        pythondata = JSONParser().parse(stream)
        # python to complex data convert
        serializer = Aiquestserializer(data=pythondata)

        if serializer.is_valid():
            serializer.save()
            res = {"msg": " Successfully insert data!"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type="application/json")
