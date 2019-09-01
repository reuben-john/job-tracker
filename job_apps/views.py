from django.shortcuts import render

# Create your views here.
from .models import Application


def index(request):
    """The home page for Job Tracker."""
    return render(request, 'job_apps/index.html')


def job_log(request):
    """List of all job log entries for user"""
    job_log = Application.objects.order_by('date_added')
    context = {'job_log': job_log}
    return render(request, 'job_apps/job_log.html', context)
