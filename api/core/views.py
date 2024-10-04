from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CutSerializer
from rest_framework import status
from .forms import CutForm, RollFormSet
from django.shortcuts import render, redirect
from .models import Cut, Roll, Producer, SewingHouseWorker


class CutCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
        
    

