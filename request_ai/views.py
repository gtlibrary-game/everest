from django.shortcuts import render

from rest_framework import viewsets
from .models import AIRequest
from .serializers import AIRequestSerializer

class AIRequestViewSet(viewsets.ModelViewSet):
    queryset = AIRequest.objects.all()
    serializer_class = AIRequestSerializer
    
    # Add your method to handle AI requests here

