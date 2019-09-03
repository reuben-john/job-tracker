from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
from .models import Application
from .forms import ApplicationForm


def index(request):
    """The home page for Job Tracker."""
    return render(request, 'job_apps/index.html')


@login_required
def job_log(request):
    """List of all job log entries for user"""
    job_log = Application.objects.filter(
        owner=request.user).order_by('date_added')
    context = {'job_log': job_log}
    return render(request, 'job_apps/job_log.html', context)


@login_required
def job_entry(request, job_entry_id):
    """Show details for a single job log"""
    job_entry = Application.objects.filter(id=job_entry_id).values()
    job_title = Application.objects.get(id=job_entry_id)
    check_log_owner(job_title.owner, request.user)

    context = {'job_title': job_title, 'job_entry': job_entry}
    return render(request, 'job_apps/job_entry.html', context)


@login_required
def new_job_entry(request):
    """Add a new job application entry"""
    if request.method != 'POST':
        # No data submitted, create blank form
        form = ApplicationForm()

    else:
        # POST data submitted, process data
        form = ApplicationForm(data=request.POST)
        if form.is_valid():
            new_job_entry = form.save(commit=False)
            new_job_entry.owner = request.user
            new_job_entry.save()
            return redirect('job_apps:job_log')

    # Display blank or invalid form
    context = {'form': form}
    return render(request, 'job_apps/new_job_entry.html', context)


@login_required
def edit_job_entry(request, job_entry_id):
    """Edit existing job entry"""
    job_entry = Application.objects.get(id=job_entry_id)
    check_log_owner(job_entry.owner, request.user)

    if request.method != 'POST':
        # Initial request, pre-fill form with current data
        form = ApplicationForm(instance=job_entry)

    else:
        # POST data submitted, process data
        form = ApplicationForm(instance=job_entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_apps:job_log')

    context = {'job_entry': job_entry, 'form': form}
    return render(request, 'job_apps/edit_job_entry.html', context)


def check_log_owner(owner, user):
    # Make sure the topic belongs to current user
    if owner != user:
        raise Http404
