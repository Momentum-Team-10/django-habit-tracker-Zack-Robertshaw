from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, action
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.reverse import reverse 

from core.models import Habit, Record
from .permissions import IsOwnerOrReadOnly
from .serializers import HabitSerializer, RecordSerializer


# Create your views here.

@api_view(['GET']) 
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        # 'api_home' might be wrong
        'habits': reverse('api_home', request=request, format=format)
    })

class HabitListView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitDetailView(RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    
    

class RecordListView(ListAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

class RecordDetailView(RetrieveAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer