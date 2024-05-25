from django.db import models
from django.utils import timezone

# Create your models here.
class Course(models.Model):
    LANGUAGE_TYPE=[
        ('EN','ENGLISH'),
        ('HI','HINDI'),
        ('MR','MARATHI')
    ]
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to="templatePrac/")
    date_added=models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=2,choices=LANGUAGE_TYPE)

    def __str__(self):
        return self.name
