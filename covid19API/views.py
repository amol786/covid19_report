from django.shortcuts import render
from rest_framework import generics
from .models import CovidReport
from .serializers import CovidReportSerialozer

# Create your views here.
class ListCovidReportView(generics.ListAPIView):
    queryset = CovidReport.objects.all()
    serializer_class = CovidReportSerialozer