from rest_framework import serializers
from .models import CovidReport

class CovidReportSerialozer(serializers.ModelSerializer):
    class Meta:
        model = CovidReport
        fields ='__all__'


