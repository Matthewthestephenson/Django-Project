from django.db import models
#from django.conf import settings
import os

class Project(models.Model):
    SETTINGS_DIR = os.path.dirname(os.path.realpath(__file__))
    PROJECT_PATH = os.path.abspath(os.path.join(SETTINGS_DIR, '..'))
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    
    image = models.ImageField(upload_to='media/img/projects', verbose_name='imagey boi')

# Create your models here.
