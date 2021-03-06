This is a Django project with scheduled tasks to collect data from Facebook. Django is a high-level Python Web framework. Celery is a task queue with focus on real-time processing, while also supporting task scheduling. Redis is a message broker. This means it handles the queue of "messages" between Django and Celery.
This project is written for Python 3

## Instructions
1. You need install dependencies
    ```
    pip install -r requirements.txt
    ```
2. These application use database tables, so we need to create the tables in the database before we can use them. To do that, run the following command:
    ```
    python manage.py migrate
    ```
3. To include the facebook app run another command:
    ```
    python manage.py makemigrations facebook
    ```
4. Run migrate again to create those model tables in database:
    ```
    python manage.py migrate
    ```
5. To run the project do:
    ```
    python manage.py runserver
    ```
6. Download redis. Open and test Redis:

    redis-cli ping
    ```
    $ redis-cli ping
    PONG
    ```
    redis-server
    ```
    $ redis-server
    ```
7.  Test task. Open a terminal window and run celery worker
    ```
    celery -A socialbuzz worker -l info -P eventlet
    ```
8. Test scheduled tasks with Celery Beat. Open another terminal window to run scheduled tasks:
    ```
    celery -A socialbuzz beat -l info -S django
    ```
