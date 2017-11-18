from django.shortcuts import render
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet

from jobs.models import Job
from jobs.serializers import JobSerializer

from .models import Company
from .serializers import CompanySerializer

class CompanyAPI(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @detail_route()
    def jobs(self,request,pk=None):
        #print("HELLO THERE")
        company = self.get_object()
        qs = Job.objects.filter(company=company)
        serializer = JobSerializer(qs,many=True)
        return Response(serializer.data,status = 200,content_type="application/json")

