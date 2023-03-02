from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerializer

@api_view(['GET', 'POST'])
def contact(request):
    
    if request.method == 'GET':
        return Response({'message': 'Hello from the contact API endpoint', 'uri': request.build_absolute_uri()})
    
    elif request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)