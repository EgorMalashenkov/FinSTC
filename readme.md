Setup:

    python3.8 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver

db:

    docker-compose up

api doc:

    /swagger/
