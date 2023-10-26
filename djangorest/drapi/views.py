from django.shortcuts import render
from .serializers import Aiquestserializer
from .models import Aiquest
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.


# Queryset
def aiquest_info(register):
    # complex data
    ai = Aiquest.objects.all()
    # python dict/native python data
    serializer = Aiquestserializer(ai, many=True)
    # render json
    json_data = JSONRenderer().render(serializer.data)
    # json sent to user/display/Front-End
    return HttpResponse(json_data, content_type="application/json")


# model instance
def aiquest_ins(register, pk):
    # complex data
    ai = Aiquest.objects.get(id=pk)
    # python dict/native python data
    serializer = Aiquestserializer(ai)
    # render json
    json_data = JSONRenderer().render(data=serializer.data)
    # json sent to user/display/Front-End
    return HttpResponse(json_data, content_type="application/json")
