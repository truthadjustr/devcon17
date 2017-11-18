from django.shortcuts import render
from django.views.generic import ListView

from rest_framework.viewsets import ModelViewSet
from .models import Job
from .serializers import JobSerializer

# Create your views here.
class JobList(ListView):
    model = Job
    #template = 

class ArcanysJobList(ListView):
    model = Job
    queryset = Job.objects.filter(company__name = 'Arcanys')

class JobAPI(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

