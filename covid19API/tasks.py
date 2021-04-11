
from time import sleep
from bs4 import BeautifulSoup
from celery import shared_task
from .models import CovidReport
#import requests
from urllib.request import urlopen, Request

@shared_task
#some heavy data
def create_coviddata():
    print('Creating Covidapi  data ..')
    req = Request('https://www.worldometers.info/coronavirus/', headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    bs = BeautifulSoup(html, 'html.parser')
    scrap_data = bs.find("tbody").find_all("tr",style="")[1:]

    for idx, data in enumerate(scrap_data, 1):
        val = [i for i in data.contents if i!='\n']
        id_val = val[0].text
        country = val[1].text
        total_case = val[2].text
        total_death = val[4].text
        total_recovered = val[6].text
        active_case = val[8].text
        population = val[14].text
        #error handling fo 'N/A' value in total recovered case 
        try:
            int_total_cases = int(total_case.replace(',',""))
            int_total_recovered = int(total_recovered.replace(',',""))
            int_population = int(population.replace(',',""))
            recovery_rate = '%.2f'%(int_total_recovered/int_total_cases)
            per_pop_infected  = '%.2f'%((int_total_cases/int_population)*100)
        
        except:
            int_total_cases = int(total_case.replace(',',""))
            int_total_recovered = 0
            int_population = int(population.replace(',',""))
            recovery_rate = '%.2f'%(int_total_recovered/int_total_cases)
            per_pop_infected  ='%.2f'%((int_total_cases/int_population)*100)

        print({'id':id_val, 'country':country, 'total_case':total_case,'total_death': total_death,'total_recovered':total_recovered,
        'active_case':active_case,'population':population,'recovery_rate':recovery_rate,'per_pop_infected':per_pop_infected})
        CovidReport.objects.create(
            country=country,
            total_case=total_case,
            total_death=total_death,
            total_recovered=total_recovered,
            active_case=active_case,
            population=population,
            recovery_rate=recovery_rate,
            percentage_population_infected=per_pop_infected,
        )

        sleep(5)
    
@shared_task
#some heavy dat
def update_coviddata():
    req = Request('https://www.worldometers.info/coronavirus/', headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    bs = BeautifulSoup(html, 'html.parser')
    scrap_data = bs.find("tbody").find_all("tr",style="")[1:]
    
    for idx, data in enumerate(scrap_data, 1):
        val = [i for i in data.contents if i!='\n']
        id_val = val[0].text
        country = val[1].text
        total_case = val[2].text
        total_death = val[4].text
        total_recovered = val[6].text
        active_case = val[8].text
        population = val[14].text

        try:
            int_total_cases = int(total_case.replace(',',""))
            int_total_recovered = int(total_recovered.replace(',',""))
            int_population = int(population.replace(',',""))
            recovery_rate = '%.2f'%(int_total_recovered/int_total_cases)
            per_pop_infected  = '%.2f'%((int_total_cases/int_population)*100)
        
        except:
            int_total_cases = int(total_case.replace(',',""))
            int_total_recovered = 0
            int_population = int(population.replace(',',""))
            recovery_rate = '%.2f'%(int_total_recovered/int_total_cases)
            per_pop_infected  ='%.2f'%((int_total_cases/int_population)*100)
        
        data = {'country':country, 'total_case':total_case,'total_death': total_death,'total_recovered':total_recovered,
        'active_case':active_case,'population':population,'recovery_rate':recovery_rate,'percentage_population_infected':per_pop_infected}
        
        CovidReport.objects.filter(country=country).update(**data)
        sleep(5)
    
create_coviddata()
while True:
    sleep(15)
    update_coviddata()
