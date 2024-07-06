from django.urls import path, include
from .views import  CountryAPIView, ServiceAPIView, TextAPIView, AvailibilityAPIView
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


router=routers.SimpleRouter()
router.register("country", CountryAPIView)
router.register("service", ServiceAPIView)
router.register("text", TextAPIView)
router.register("availibility", AvailibilityAPIView)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    
    
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
]
