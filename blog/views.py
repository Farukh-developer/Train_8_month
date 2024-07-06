from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.viewsets import  ModelViewSet
from .models import Country_range, Servicetype, Text, Availibilties, Information
from .serializers import (CountrySerializer, ServiceSerializer, TextSerializer, AvailibilitySerializer, InformationSerializer)


class CountryAPIView(ModelViewSet):
    queryset=Country_range.objects.all()
    serializer_class=CountrySerializer


class ServiceAPIView(ModelViewSet):
    queryset=Servicetype.objects.all()
    serializer_class=ServiceSerializer
    
    
    

class TextAPIView(ModelViewSet):
    queryset=Text.objects.all()
    serializer_class=TextSerializer    
       

class AvailibilityAPIView(ModelViewSet):
    queryset=Availibilties.objects.all()
    serializer_class=AvailibilitySerializer    




class InformationAPIView(ModelViewSet):
    queryset=Information.objects.all()
    serializer_class=InformationSerializer    
    