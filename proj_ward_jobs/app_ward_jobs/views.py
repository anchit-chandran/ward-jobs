from django.shortcuts import render

# Create your views here.
def home(request):
    
    jobs = [
        {
            'patient_name' : 'Anchit',
            'patient_dob' : '18/10/1997',
            'hospital_number' : 'RXR12345678',
            'job' : 'Order bloods FBC, U+Es, CRP',
        },
        {
            'patient_name' : 'Brian',
            'patient_dob' : '18/10/1997',
            'hospital_number' : 'RXR1231235',
            'job' : 'Order MRI Head',
        },
        {
            'patient_name' : 'Charlie',
            'patient_dob' : '18/10/2015',
            'hospital_number' : 'RXR1262238',
            'job' : 'Review PM for stretch inhalers',
        },
    ]
    
    return render(request, template_name='app_ward_jobs/home.html', context={'jobs':jobs})