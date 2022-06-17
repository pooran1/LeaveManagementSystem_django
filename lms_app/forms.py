
from dataclasses import field
from pyexpat import model
from unicodedata import category
from django.forms import ModelForm
# from .models import TODO
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import LeaveBank, Leave_type, Profile, Role, Department, Category, Permission


# class TODOForm(ModelForm):
#     class Meta:
#         model = TODO
#         fields = ['title', 'status', 'priority']


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    reporting_manager = forms.ModelChoiceField(
        queryset=User.objects.all().exclude(is_active=False))
    contact_no = forms.CharField(max_length=50)
    leave_assign = forms.IntegerField()
    gender = forms.ChoiceField(choices=(
        ('M', 'Male'), ('F', 'Female')))
    departmant = forms.ModelChoiceField(
        queryset=Department.objects.all())
    role = forms.ModelChoiceField(
        queryset=Role.objects.all())
    permission = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.SelectMultiple()
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all())
    # status = forms.ChoiceField(choices=(
    #                           ('A', 'Active'), ('I', 'Inactive')))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')


class RegisterUserForm2(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    # reporting_manager = forms.ModelChoiceField(
    #     queryset=User.objects.all().exclude(is_active=False))
    contact_no = forms.CharField(max_length=50)
    # leave_assign = forms.IntegerField()
    gender = forms.ChoiceField(choices=(
        ('M', 'Male'), ('F', 'Female')))
    departmant = forms.ModelChoiceField(
        queryset=Department.objects.all())
    role = forms.ModelChoiceField(
        queryset=Role.objects.all())
    permission = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.SelectMultiple()
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all())
    # status = forms.ChoiceField(choices=(
    #                           ('A', 'Active'), ('I', 'Inactive')))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', ]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['reporting_manager', 'contact_no', 'leave_assign', 'Permission',
                  'gender', 'departmant', 'role', 'category', ]


class ProfileUpdateForm2(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['contact_no',
                  'gender', ]


class RoleForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    permission = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.SelectMultiple()
    )

    class Meta:
        model = Role
        fields = ['name', 'permission']


class PermissionForm(forms.ModelForm):

    class Meta:
        model = Permission
        fields = ['name', ]


class Leave_type_Form(forms.ModelForm):
    class Meta:
        model = Leave_type
        fields = ['name', ]


class LeaveCreationForm(forms.ModelForm):
    reason = forms.CharField(
        required=False, widget=forms.Textarea(attrs={'rows': 4, 'cols': 20}))
    leavetype = forms.ModelChoiceField(queryset=Leave_type.objects.all())

    class Meta:
        model = LeaveBank
        exclude = ['user', 'status', 'is_approved', ]

# class Apply_leave_form(forms.ModelForm):
#     class Meta:
#         model = LeaveBank
#         fields = ['start_date', 'end_date', 'leavetype', 'reason']
