from django.shortcuts import render
from rest_framework.decorators import detail_route
from rest_framework.response import Response

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

    '''
    #@detail_route(methods=['post'])
    @detail_route()
    def apply(self,request,pk=None):
        application = request.data.get('application_id')                 
        applicant = User.objects.get(pk=application_id)
        job = self.get_object()
        Application.objects.create(applicant = applicant,job = job)
        return Response(serializer.data,status = 200,content_type = "application/json")
    '''
