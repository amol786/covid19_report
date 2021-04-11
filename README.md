# Covid19 Real Time Report
Covud19 Real Time API built with Beautiful Soup & Django REST Framework

Install dependencies:

python3 -m pip3 install -r requirements.txt
run following commands:

python manage.py makemigrations covid19API
python manage.py migrate
python manage.py runserver

and start Celery worker:

celery -A Covid19 worker -l info
