from django.db import models
from django.utils import timezone

# Create your models here.


GENDER =(
    ('MALE' , 'MALE'),
    ('FEMAIL' , 'FEMAIL')
)


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=2000)
    active = models.BooleanField(default = False)
    created_at = models.DateField(default=timezone.now)
    edited_At = models.DateTimeField(default=timezone.now)
    emil = models.EmailField(default= '')
    gender = models.CharField(choices=GENDER , max_length=10)