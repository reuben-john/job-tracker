from django.db import models

# Create your models here.


class Application(models.Model):
    '''An application the user has submitted'''
    STATUSES = [('submitted', 'SUBMITTED'),
                ('accepted', 'ACCEPTED'),
                ('rejected', 'REJECTED')]
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    post_url = models.CharField(max_length=300)
    contact_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date_added = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUSES)
