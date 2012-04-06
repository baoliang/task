from service.task import convert_media 
from celery.decorators import task

@task    
def convert_task():
    convert_media()
