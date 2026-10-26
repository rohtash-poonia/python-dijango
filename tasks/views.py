from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hello_world(request):
    """
    GET hello
    A simple view that returns a JSON response with a greeting message.
    """
    return Response({"message": "Hello, World!"})