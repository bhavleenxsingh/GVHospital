from django.db import models
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField

Department_Choices = [
    ('Cardio', 'Cardiology'),
    ('Neuro', 'Neurology'),
    ('Pedia', 'Pediatrician'),
    ('Ortho', 'Orthopedic'),
    ('General', 'General'),
    ('Onco', 'Oncology')
]

Gender_Choices = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other')    
]
# Create your models here.
class docreg(models.Model):
    Username = models.CharField(max_length = 20)
    Password = models.CharField(max_length = 25)
    ConfirmPassword = models.CharField(max_length = 25)
    Time = models.DateTimeField(default = datetime.now())
    
    def __str__(self):
        return f'{self.Username} {self.Password} {self.Time}'
   
class doclogin(models.Model):
    Username = models.CharField(max_length = 20)
    Password = models.CharField(max_length = 25)
    Time = models.DateTimeField(default = datetime.now())
        
    def __str__(self):
        return f'{self.Username} and {self.Password}, {self.Time}'

class nursereg(models.Model):
    Username = models.CharField(max_length = 20)
    Password = models.CharField(max_length = 25)
    ConfirmPassword = models.CharField(max_length =25, default="")
    Time = models.DateTimeField(default = datetime.now())
    
    def __str__(self):
        return f'{self.Username}, {self.Password}, {self.Time}'
 
class nurselogin(models.Model):
    Username = models.CharField(max_length = 20)
    Password = models.CharField(max_length = 25)
    Time = models.DateTimeField(default = datetime.now())
    
    def __str__(self):
        return f'{self.Username} {self.Password} {self.Time}'
        
class patientinfo(models.Model):
    FirstName = models.CharField(max_length = 50)
    LastName = models.CharField(max_length = 50)
    Gender = models.CharField(max_length = 1, choices= Gender_Choices, default="O")
    Mobile = PhoneNumberField()
    Department = models.CharField(max_length =7, choices = Department_Choices, default = " ")
    Time = models.DateTimeField(default = datetime.now())
    
    def __str__(self):
        return f'{self.FirstName}, {self.LastName}, {self.Mobile}'
    
class feedback(models.Model):
    Name = models.CharField(max_length = 50)
    Mobile = PhoneNumberField()
    Email = models.CharField(max_length=35)
    Message = models.CharField(max_length=200)
    Time = models.DateTimeField(default = datetime.now())

    def __str__(self):
        return f'{self.Name}, {self.Mobile}, {self.Email}, {self.Message}'