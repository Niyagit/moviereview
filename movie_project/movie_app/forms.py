# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

# class UserRegistrationForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email', 'password']

#     def save(self, commit=True):
#         user = super(NewUserForm, self).save(commit=False)
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#         return user

# # class MovieForm(forms.ModelForm):
# #     class Meta:
# #         model = Movie
# #         exclude = ['user']

# # class ReviewForm(forms.ModelForm):
# #     class Meta:
# #         model = Review
# #         exclude = ['user', 'movie']
from django import forms 
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .models import Movie, Review

from django.forms import ModelForm, ValidationError
# class SignupForm(UserCreationForm):
    
#     username = forms.CharField(widget=forms.TextInput(attrs={
#         "class": "input",
#         "type": "text",
#         "placeholder": "enter username"
#     }))
#     first_name = forms.CharField(widget=forms.TextInput(attrs={
#         "class": "input",
#         "type": "text",
#         "placeholder": "enter username"
#     }))
#     last_name = forms.CharField(widget=forms.TextInput(attrs={
#         "class": "input",
#         "type": "text",
#         "placeholder": "enter last name"
#     }))


#     email = forms.CharField(widget=forms.TextInput(attrs={
#         "class": "input",
#         "type": "email",
#         "placeholder": "enter email-id"
#     }))

#     password1 = forms.CharField(widget=forms.TextInput(attrs={
#         "class": "input",
#         "type": "password",
#         "placeholder": "enter password"
#     }))

#     password2 = forms.CharField(widget=forms.TextInput(attrs={
#         "class": "input",
#         "type": "password",
#         "placeholder": "re-enter password"
#     }))

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', "password2"]

# class LoginForm(forms.Form):
#     username = forms.CharField(widget=forms.TextInput(attrs={
#         "class": "input",
#         "type": "password",
#         "placeholder": "enter username"
#     }))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={
#         "class": "input",
#         "type": "password",
#         "placeholder": "enter password"
#     }))

	

# class SignupForm(forms.ModelForm):
# 	username = forms.CharField(widget=forms.TextInput(), max_length=30, required=True)
# 	email = forms.CharField(widget=forms.EmailInput(), max_length=100, required=True)
# 	first_name = forms.CharField(widget=forms.TextInput(), max_length=50, required=True)
# 	last_name = forms.CharField(widget=forms.TextInput(), max_length=50, required=True)
# 	password = forms.CharField(widget=forms.PasswordInput())
# 	confirm_password = forms.CharField(widget=forms.PasswordInput(), required=True, label='Confirm your password.')

# 	class Meta:
# 		model = User
# 		fields = ('username', 'email', 'first_name','last_name', 'password')

# 	def __init__(self, *args, **kwargs):
# 		super(SignupForm, self).__init__(*args, **kwargs)
# 		self.fields['username'].validators.append(UniqueUser)
# 		self.fields['email'].validators.append(UniqueEmail)

# 	def clean(self):
# 		super(SignupForm, self).clean()
# 		password = self.cleaned_data.get('password')
# 		confirm_password = self.cleaned_data.get('confirm_password')

# 		if password != confirm_password:
# 			self._errors['password'] = self.error_class(['Password do not match. Try again'])
# 		return self.cleaned_data

class EditUserProfileForm(UserChangeForm):
    # username = forms.CharField(max_length=150,widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':"enter user  name"}))
    # first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"enter your first name"}))
    # last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"enter your last name"}))
    # email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':"enter user  name"}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

class Movieform(forms.ModelForm):
      class Meta:
         model=Movie
         fields=['title','poster','description','release_date','actors','category','trailer_link']    

# from django import forms

# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=100)
#     password = forms.CharField(widget=forms.PasswordInput)
class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
    

class RegisterForm(UserCreationForm):

    class Meta:
        model=User
        fields = ['username','email','password'] 


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("comment", "rating")


   
        