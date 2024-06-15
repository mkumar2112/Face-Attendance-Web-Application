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
    

def employee_image_path(instance, filename):
    filename = f'{filename}'
    print(filename)
    return os.path.join('static/EmployeeImages/', filename)

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

class Attendance(models.Model):
    Attend_Id = models.AutoField(primary_key=True)
    Date = models.DateField(auto_now=True)
    Time = models.TimeField(auto_now=True)
    Emp_id = models.ForeignKey(EmployeeDetails, on_delete=models.CASCADE, default="1")
    Today_Attendence = models.BooleanField(default=False)
    

    def __str__(self):
        return f"Attendance for {self.Emp_id.Name} on {self.Date}", self.Emp_id.Emp_id















'''
Shell Commands

To delete all records
from Home.models import EmployeeDetails
EmployeeDetails.objects.all().delete()


To Reterive all records
from Home.models import EmployeeDetails
EmployeeDetails.objects.all()

retrieves a single record
record = YourModel.objects.get(id=1)

returns a queryset containing all records that match the given criteria.
YourModel.objects.filter(name='John')

returns a queryset containing all records that do not match the given criteria.
YourModel.objects.exclude(name='John')

first record in the queryset, or None if the queryset is empty.
YourModel.objects.first()

returns the last record
YourModel.objects.last()

order_by(): The order_by() method orders the queryset based on the given field(s). Prefixing a field name with - indicates descending order.
YourModel.objects.order_by('name')

returns a queryset that returns dictionaries for each record, containing only the specified field(s).
YourModel.objects.values('name', 'age')

returns the number of records
num_records = YourModel.objects.count()


'''



'''
Update Your database
from yourapp.models import YourModel

# Get the record you want to update
record = YourModel.objects.get(id=1)

# Update the values
record.field1 = 'new value'
record.field2 = 'another new value'

# Save the changes
record.save()
'''