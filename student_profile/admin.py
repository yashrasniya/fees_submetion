from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Student


class User(UserAdmin):
    list_display = ('mobile_number', 'roll_number', 'branch', 'batch')

    # def has_change_permission(self, request, obj=None):
    #     return False
    #
    # # def has_add_permission(self, request):
    # #     return False
    #
    # def has_delete_permission(self, request, obj=None):
    #     return False


admin.site.register(Student, User)
