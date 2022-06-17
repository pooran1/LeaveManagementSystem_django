from django.contrib import admin

# Register your models here.
from .models import Leave_type, LeaveBank, Permission, Profile, Role, Department, Category
# Register your models here.


admin.site.register(Profile)
admin.site.register(Role)
admin.site.register(Department)
admin.site.register(Category)
admin.site.register(Permission)
admin.site.register(Leave_type)
admin.site.register(LeaveBank)
