from celery import Celery

app = Celery('celery_main', broker='redis://localhost:6379/0')


