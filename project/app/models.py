from django.db import models
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class docreg(models.Model):
    Username = models.CharField(max_length = 20)
    Password = models.CharField(max_length = 25)
    Confirm_Password = models.CharField(max_length = 25)
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
    Password = models.CharField(max_length = 20)
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
    Mobile = PhoneNumberField()
    
    def __str__(self):
        return f'{self.FirstName}, {self.LastName}, {self.Mobile}'
    
class feedback(models.Model):
    Name = models.CharField(max_length = 50, null = False, blank = False)
    Mobile = PhoneNumberField()
    Email = models.EmailField()
    Message = models.TextField()
    Time = models.DateTimeField(default = datetime.now())

    def __str__(self):
        return f'{self.Name}, {self.Mobile}, {self.E_mail}, {self.Message}'