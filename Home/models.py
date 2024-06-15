from django.db import models
import os

# Create your models here.
# SuperUser -> monu -> 123



# Creating our Contact model and save there fields.
class Contacts(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=254)
    Contact = models.IntegerField(null=False)
    Address = models.CharField(max_length=500)
    City = models.CharField(max_length=500)
    State = models.CharField(max_length=500)
    Zip = models.IntegerField() 

    # def __str__(self):
    #     return self.First_Name
    
# Add image to employee path function
def employee_image_path(instance, filename):
    filename = f'{filename}'
    print(filename)
    return os.path.join('static/EmployeeImages/', filename)

# Employee Details Table.
class EmployeeDetails(models.Model):
    Emp_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50, null=False)
    Email = models.EmailField(max_length=50, null=False)
    Contact = models.CharField(max_length=15, null=False)  # Changed to CharField to accommodate different formats
    Age = models.IntegerField()
    Dob = models.DateField(auto_now=False, auto_now_add=False)
    Joining_Date = models.DateField(auto_now=True)
    Total_Attendence = models.IntegerField(default=0)
    img = models.ImageField(upload_to=employee_image_path)

    def __str__(self):
        return str(self.Emp_id)

# Attendance Table
class Attendance(models.Model):
    Attend_Id = models.AutoField(primary_key=True)
    Date = models.DateField(auto_now=True)
    Time = models.TimeField(auto_now=True)
    Emp_id = models.ForeignKey(EmployeeDetails, on_delete=models.CASCADE, default="1")
    Today_Attendence = models.BooleanField(default=False)
    

    def __str__(self):
        return f"Attendance for {self.Emp_id.Name} on {self.Date}", self.Emp_id.Emp_id














