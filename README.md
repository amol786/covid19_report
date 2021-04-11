# Covid19 Real Time Report
Covud19 Real Time API built with Beautiful Soup & Django REST Framework

Install dependencies:

python3 -m pip3 install -r requirements.txt <br>
run following commands:

python manage.py makemigrations covid19API <br>
python manage.py migrate <br>
python manage.py runserver <br>

and start Celery worker: 

celery -A Covid19 worker -l info
