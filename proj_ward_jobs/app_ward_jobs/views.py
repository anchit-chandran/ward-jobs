from django.shortcuts import render

from .models import Patient, Doctor, Job

# Create your views here.


def home(request):

    jobs = Job.objects.all()

    context = {
        'jobs': jobs
    }
    return render(request, template_name='app_ward_jobs/home.html', context=context)


def all_jobs(request):

    jobs = Job.objects.all()

    context = {
        'jobs': jobs
    }

    return render(request, template_name='app_ward_jobs/all_jobs_list.html', context=context)
