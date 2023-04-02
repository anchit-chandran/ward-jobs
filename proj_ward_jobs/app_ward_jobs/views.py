from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Patient, Doctor, Job
from .forms import AddJobForm

# Create your views here.


def home(request):

    jobs = Job.objects.all()

    context = {
        'jobs': jobs
    }
    return render(request, template_name='app_ward_jobs/home.html', context=context)


def add_job(request):

    if request.method == 'POST':

        form = AddJobForm(request.POST)
        
        if form.is_valid():
            form.save()

        return redirect(reverse('home'))

    else:

        form = AddJobForm()

    return render(request, 'app_ward_jobs/add_job.html', context={'form':form})


def all_jobs(request):

    jobs = Job.objects.all()

    context = {
        'jobs': jobs
    }

    return render(request, template_name='app_ward_jobs/all_jobs_list.html', context=context)
