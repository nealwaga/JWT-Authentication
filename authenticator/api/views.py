from uuid import RESERVED_FUTURE
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import *
from .serializer import *


# Create your views here.
class HelloWorld(APIView):
    permission_classes = (IsAuthenticated, )
    
    def get(self, request):
        content = {
            'message': 'Hello World'
        }
        return Response(content)
    
    
class Extractor(APIView):
    permission_classes = (IsAuthenticated, )
    
    def get(self, request):
        content = {
            'username': request.user.username,
            'password': request.user.password,
        }
        return Response(content)
    
    
# class EmployeeList(APIView):

#     #to return all employees in the model
#     def get(self, request):
#         employess1 = Employees.objects.all() #variable to store all my objects
#         serializer = EmployeesSerializer(employess1, many=True) #taking all objects & converting them to JSON
#         return Response(serializer.data)

#     #to create a new employee
#     def post(self):
#         pass
