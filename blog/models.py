from django.db import models

# Create your models here.
class Country_range(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Text(models.Model):
    text=models.CharField(max_length=50)
    image=models.ImageField(upload_to='umra_pict/', null=True, blank=True)
    phone_num=models.IntegerField()
       
    
class Servicetype(models.Model):
    type=models.CharField(max_length=50)    
  
    def __str__(self):
        return self.type    
    
class Availibilties(models.Model):
    price=models.IntegerField()
    duration=models.DurationField()
    meal=models.CharField(max_length=50)
    medical_care=models.CharField(max_length=20)
    guidelines=models.CharField(max_length=10)
    provided_appliances=models.CharField(max_length=100)
    servicetype=models.ForeignKey(Servicetype, on_delete=models.CASCADE, related_name='availabilities')
    country=models.ForeignKey(Country_range, on_delete=models.CASCADE, related_name='availabilities')
    
    def __str__(self):
        return f'{self.servicetype.type} in {self.country.name}'
    
class Information(models.Model):
    detail=models.CharField(max_length=500)
    links=models.CharField(max_length=40)
           