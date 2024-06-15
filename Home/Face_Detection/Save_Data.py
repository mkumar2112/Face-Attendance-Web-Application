from django.core.mail import send_mail
from django.utils import timezone
from Home.models import EmployeeDetails, Attendance
from django.db import transaction

def Attendence_True(Person_id):
    # Fetch the employee details
    try:
        employee = EmployeeDetails.objects.get(Emp_id=Person_id)
    except EmployeeDetails.DoesNotExist:
        print(f"Employee with id {Person_id} does not exist.")
        return

    try:
        with transaction.atomic():
            # Create and save the attendance record
            Today_All_Present_object = Attendance.objects.filter(Date=timezone.now().date()) # Return a Attendence object.
            Today_All_Present_Employees = [i.Emp_id.Emp_id for i in Today_All_Present_object]
            if Person_id in Today_All_Present_Employees:
                print('Person Already marked Present')
            else:
                Attendance.objects.create(
                    Emp_id=employee,
                    Today_Attendence=True
                )
                # Calculate total attendance
                total_attendance = employee.Total_Attendence + 1
                # Update the employee details
                employee.Today_Attendence = True
                employee.Total_Attendence = total_attendance
                employee.save()
                try:
                    send_mail(
                    "Attandance Marked",
                    f"Dear {employee.Name}, \n\n Your Attandance is marked. \nTotal Attandance = {employee. Total_Attendence}",
                    "mkumar321568@gmail.com",
                    [employee.Email],
                    fail_silently=False,
                    )
                except e:
                    print(e)
            


            # print('Updated')
    except Exception as e:
        print('Not Updated:', e)












'''
Attandence True:
employee = EmployeeDetails.objects.get(Emp_id=20)
employee.Today_Attendence = False
employee.save()

'''