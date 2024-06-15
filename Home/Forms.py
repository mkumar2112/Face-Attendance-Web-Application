from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contacts


class Contact_Form(forms.Form):
    First_Name = forms.CharField(label='First Name', max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'First Name'}) )
    Last_Name = forms.CharField(label='Last Name',max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    Email_Name = forms.EmailField(label='Email',max_length=254, required=True, widget=forms.TextInput(attrs={'placeholder': 'abc123@gmail.com'}))
    Contact = forms.CharField(label='Contact No.', max_length=10, widget=forms.TextInput(attrs={'placeholder': '12345-67890'}))
    Address = forms.CharField(label='Address',max_length=500, widget=forms.TextInput(attrs={'placeholder': 'Address'}))
    City = forms.CharField(label='City',max_length=500, widget=forms.TextInput(attrs={'placeholder': 'Aali Vihar'}))
    State = forms.CharField(label='State',max_length=500,widget=forms.TextInput(attrs={'placeholder': 'Delhi'}))
    Zip = forms.CharField( label='Zip', max_length=6,  widget=forms.TextInput(attrs={'placeholder': '111000'}) )
    
    def save(self):
        contact = Contacts(
            First_Name=self.cleaned_data['First_Name'],
            Last_Name=self.cleaned_data['Last_Name'],
            Email=self.cleaned_data['Email_Name'],
            Contact=self.cleaned_data['Contact'],
            Address=self.cleaned_data['Address'],
            City=self.cleaned_data['City'],
            State=self.cleaned_data['State'],
            Zip=self.cleaned_data['Zip']
        )
        contact.save()
        return contact
    # class Meta:
    #     model = Contacts
    #     fields = ["username", "email","password1", "password2"]


# Creating Forms for create user...
class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(
        label='Password', 
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),  
        help_text="Including A-Z, a-z, and 0-9. and Must have 8 letters"
    )
    password2 = forms.CharField(
        label='Confirm Password', 
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}), 
        help_text="Enter the same password as above, for verification."
    )


    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class AddEmployee(forms.Form):
    Name = forms.CharField(label='Name', max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    Email = forms.EmailField(label='Email', max_length=254, required=True, widget=forms.TextInput(attrs={'placeholder': 'abc123@gmail.com'}))
    Contact = forms.CharField(label='Contact No.', max_length=10, widget=forms.TextInput(attrs={'placeholder': '12345-67890'}))
    Age = forms.IntegerField(label='Age', widget=forms.TextInput(attrs={'placeholder': 'Age'}))
    Dob = forms.DateField(widget=forms.SelectDateWidget(years=range(1980, 2010)))
    img = forms.ImageField()