from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views 


urlpatterns = [
    
    path ('registration', jwt_views.TokenObtainPairView.as_view(), name='registration'),
    path ('login', jwt_views.TokenObtainPairView.as_view(), name='login'),
    
    path ('run', views.HelloWorld.as_view(), name='hello-world'),
    path ('me', views.Extractor.as_view(), name='extract-token'),
    
    # path('employees', views.EmployeeList.as_view(), name='employee-list'),
]