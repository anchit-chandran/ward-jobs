from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('view-all-jobs', views.all_jobs, name='all-jobs'),
]