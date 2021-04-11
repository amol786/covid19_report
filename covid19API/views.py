from django.shortcuts import render
from rest_framework import generics, filters,pagination
from .models import CovidReport
from .serializers import CovidReportSerialozer

from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000

class ListCovidReportView(generics.ListAPIView):
    queryset = CovidReport.objects.all()
    serializer_class = CovidReportSerialozer
    #filter_backends = [DjangoFilterBackend]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    #filterset_fields = ['country',]
    search_fields = ['country', ]
    ordering_fields = '__all__'
    pagination_class = StandardResultsSetPagination