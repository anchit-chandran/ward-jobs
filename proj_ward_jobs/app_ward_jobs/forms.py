from django import forms
from django.forms import ModelForm
from app_ward_jobs.models import Job

class AddJobForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = Job
        fields = '__all__'
        
        
