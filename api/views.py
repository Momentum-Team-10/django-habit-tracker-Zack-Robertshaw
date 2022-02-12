from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, action
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.reverse import reverse 

from core.models import Habit, Record, User
from .permissions import IsOwnerOrReadOnly
from .serializers import HabitSerializer, RecordSerializer, UserSerializer


# Create your views here.


@api_view(['GET']) 
def api_root(request, format=None):
    return Response({
        'habits': reverse('habits_list', request=request, format=format),
        'records': reverse('records_list', request=request, format=format),
        'users': reverse('users_list', request=request, format=format)
    })



class UserViewSet(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]



class HabitListView(ListCreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class HabitDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]
    
    

class RecordListView(ListCreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]

class RecordDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]
