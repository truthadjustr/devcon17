from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import Company
from .serializers import CompanySerializer

class CompanyAPI(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
