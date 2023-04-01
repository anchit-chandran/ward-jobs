from django.db import models

from django.utils import timezone

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    MALE='M'
    FEMALE='F'
    SEX_CHOICES = [
        (MALE, 'M'),
        (FEMALE, 'F')
    ]
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default=MALE)
    dob = models.DateField()
    hospital_number = models.IntegerField(unique=True)
    
    @property
    def age(self):
        today = timezone.now()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
    
    def __str__(self):
        return f"{self.get_full_name()} (AC{self.hospital_number})"
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    FY1 = 'FY1'
    FY2 = 'FY2'
    CT1 = 'CT1'
    CT2 = 'CT2'
    REGISTRAR = 'REG'
    CONSULTANT = 'CONS'
    GRADE_CHOICES = [
        (FY1, 'FY1'),
        (FY2, 'FY2'),
        (CT1, 'CT1'),
        (CT2, 'CT2'),
        (REGISTRAR, 'Registrar'),
        (CONSULTANT, 'Consultant'),
    ]
    grade = models.CharField(
        max_length=4,
        choices=GRADE_CHOICES,
        default=FY1,
    )
    
    def __str__(self):
        return f"Dr {self.first_name} {self.last_name} ({self.grade})"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

class Job(models.Model):
    description = models.CharField(max_length=500)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    assignee = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"({self.patient.get_full_name()}) {self.description[:10]}... ASSIGNED:{self.assignee.get_full_name()}"
    
    