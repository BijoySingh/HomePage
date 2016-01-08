workon homepageenv
kill $(ps aux | grep uwsgi | grep socket | awk '{print $2}')
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
uwsgi --socket :8000 --module HomePage.wsgi --chmod-socket=664 &
