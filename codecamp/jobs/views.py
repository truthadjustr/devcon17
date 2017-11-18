from django.shortcuts import render
from django.views.generic import ListView

from .models import Job

# Create your views here.
class JobList(ListView):
    model = Job
    #template = 

class ArcanysJobList(ListView):
    model = Job
    queryset = Job.objects.filter(company__name = 'Arcanys')

