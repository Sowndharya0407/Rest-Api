from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def ApiConfig(req):
    dict = {"name":"sow"}
    return Response(dict)