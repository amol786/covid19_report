from django.urls import path
from .views import ListCovidReportView, DetailCovidReportView

urlpatterns =[
    path('<int:pk>/',DetailCovidReportView.as_view()),
    path('',ListCovidReportView.as_view()),
]
