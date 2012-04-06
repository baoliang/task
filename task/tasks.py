from service.task import convert_media 
from celery.decorators import task
from service.task import update_task_data_media
@task    
def convert_task():
    convert_media()

@task
def update_task(): 
    update_task_data_media() 
