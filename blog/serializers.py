from rest_framework import serializers
from .models import Country_range, Servicetype, Availibilties, Text, Information

class CountrySerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model=Country_range
        fields='__all__'
        
class ServiceSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model=Servicetype
        fields='__all__'      
        
        
class AvailibilitySerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model=Availibilties
        fields='__all__'          
        
        
        
        
class TextSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model=Text
        fields='__all__'                  
        
        
        
class InformationSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model=Information
        fields='__all__'                          