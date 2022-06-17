

from django.db import models
from django.contrib.auth.models import User


class Permission(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'permission'


class Role(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)
    Permission = models.ManyToManyField(Permission,)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'role'


class Department(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'department'


class Category(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'


class Profile(models.Model):

    reporting_manager = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    profile_user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile_user')
    contact_no = models.CharField(max_length=50)
    leave_assign = models.IntegerField(null=True, blank=True)
    gender = models.CharField(
        max_length=2, choices=(('M', 'Male'), ('F', 'Female')))
    departmant = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    Permission = models.ManyToManyField(Permission,)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # status = models.CharField(max_length=2, choices=(
    #                           ('A', 'Active'), ('I', 'Inactive')), blank=False, null=True)

    class Meta:
        db_table = 'profile'


class Leave_type(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'leave_type'


class LeaveBank(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    start_date = models.DateField(
        help_text='    leave start date is on ..', null=True, blank=False)
    end_date = models.DateField(
        help_text='   coming back on ...', null=True, blank=False)
    leavetype = models.ForeignKey(Leave_type, on_delete=models.CASCADE)
    reason = models.CharField(
        max_length=255, help_text='add additional information for leave', null=True, blank=True)
    # pending,approved,rejected,cancelled
    status = models.CharField(max_length=12, default='pending')
    is_approved = models.BooleanField(default=False)

#
