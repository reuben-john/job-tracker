from django.shortcuts import render

# Create your views here.


def index(request):
    """The home page for Job Tracker."""
    return render(request, 'job_apps/index.html')
