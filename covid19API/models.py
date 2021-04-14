from django.db import models

# Create your models here.
class CovidReport(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=40)
    total_case = models.CharField(max_length=500)
    total_death = models.CharField(max_length=500)
    total_recovered = models.CharField(max_length=500)
    active_case = models.CharField(max_length=500)
    population = models.CharField(max_length=500)
    recovery_rate = models.CharField(max_length=10,null=True,blank=True)
    percentage_population_infected = models.CharField(max_length=10,null=True,blank=True)
  
    class Meta:
        verbose_name = 'CovidReport'
        verbose_name_plural='CovidReports'


    def __str__(self):
        return self.country