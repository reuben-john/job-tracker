from django.db import models
from django.contrib.auth.models import User

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
    status = models.CharField(
        max_length=20, choices=STATUSES, default="submitted")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.position} @ {self.company}"
