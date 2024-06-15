from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from .Forms import RegisterForm, Contact_Form, AddEmployee
from .models import EmployeeDetails, Attendance
from django.contrib.auth.decorators import login_required
from .Face_Detection.Home import Face_Attend
from django.utils import timezone
from django.contrib import messages


# Home Page
def Home(request):
    return render(request, 'logouthome.html')

# Request for login Page if user were enter correct password and user id than login other wise return to again login page
def loginuser(request):
    if request.method =='POST':
        username = request.POST.get('user_n') # Taking user-id from web page
        password = request.POST.get('passw') # Taking password from web page
        # Checking login Credintals
        user = authenticate(username=username, password=password) # if user is authenticated than user login else user = None
        print(username, password)
        if user is not None: # Checking User is not None
             # A  backend authenticated the credentials
             print('User Founded')
             login(request, user) # Login to application
             return redirect("/loggedIn/Today") # Goes to loged in web page
        else:
             print('User not found')
             messages.error(request, 'Invalid username or password')
             # No backend authenticated the credentials
             return render(request, 'logging.html') # Return to login
    return render(request, 'logging.html')



# Request to create user
def createuser(request):
    if request.method == 'GET':
        form = RegisterForm()  # Create an instance of the registration form
        return render(request, 'createuser.html', {'form': form}) 

    elif request.method == 'POST':
        form = RegisterForm(request.POST)  # Create an instance of the form with POST data
        if form.is_valid():  # Check if the form is valid
            user = form.save(commit=False)  # Save the form without committing to the database yet
            user.username = user.username.lower()  # Convert the username to lowercase
            user.save()  # Save the user to the database
            login(request, user)  # Log the user in
            return redirect('/loging')  # Redirect to the login page

        # If the form is not valid, render the form with error messages
        return render(request, 'createuser.html', {'form': form})

#Log-out User
@login_required(login_url='/Home/')
def logoutuser(request):
    logout(request) #pre-define Function
    return redirect('/Home') # return to home page

# Add Employee Details
@login_required(login_url='/Home')
def Add_face_attendance(request):
    context = {}
    if request.method == "POST":
        form = AddEmployee(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get("Name")
            email = form.cleaned_data.get("Email")
            contact = form.cleaned_data.get("Contact")
            age = form.cleaned_data.get("Age")
            dob = form.cleaned_data.get("Dob")
            image = form.cleaned_data.get("img")
            
            obj = EmployeeDetails.objects.create(
                Name=name,
                Email=email,
                Contact=contact,
                Age=age,
                Dob=dob,
                img=image
            )
            obj.save()
            print(obj)
            
    else:
        form = AddEmployee()
    context['form'] = form
    return render(request, 'add_face.html', context)

# Today Present 
@login_required(login_url='/Home')
def Today_Present(request):
    Today_All_Present_object = Attendance.objects.filter(Date=timezone.now().date())
    
    return render(request, 'today_data.html', {'All': Today_All_Present_object})


# All Present Attendance List
@login_required(login_url='/Home')
def All_Present(request):
    Today_All_Present_object = Attendance.objects.all()
    return render(request, 'total_data.html', {'All': Today_All_Present_object})

# Contact page view
@login_required(login_url='/Home')
def contact(request):
    if request.method == 'GET':
        form = Contact_Form()  # Create an instance of the contact form
        print('--->', form)
        return render(request, 'contact.html', {'form': form}) 

    elif request.method == 'POST':
        form = Contact_Form(request.POST)  # Create an instance of the form with POST data
        print('----->', form)
        if form.is_valid():  # Check if the form is valid
            # Process the data in form.cleaned_data
            form.save()  # Assuming the form has a save method
            return redirect('/Home')  # Use the URL name defined in urls.py

        # If the form is not valid, render the form with error messages
        return render(request, 'contact.html', {'form': form})
    
# Start Camera for attendance
@login_required(login_url='/Home')
def face_attendance(request):

    cam = Face_Attend(True)
    if cam == False:
        print('Error While running')
        Face_Attend(True)
    return redirect('/loggedIn/Today')





@login_required(login_url='/Home')
def AboutUs(request):
     #pre-define Function
    return render(request, 'AboutUs.html') # return to home page
