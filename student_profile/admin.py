from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Student


class User(UserAdmin):
    list_display = ('mobile_number', 'roll_number', 'branch', 'batch')
    fieldsets = (

        (("Personal info"), {"fields": ("first_name", "last_name", "email",
                                        'father_name','mother_name','birt_date',
                                        'batch', 'branch', 'roll_number','category','gender','fess_method')}),
        # (
        #     ("Permissions"),
        #     {
        #         # "fields": (
        #         #     "is_active",
        #         #     "is_staff",
        #         #     "is_superuser",
        #         #     "groups",
        #         #     "user_permissions",
        #         ),
        #     },
        # ),
        # (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    # def has_change_permission(self, request, obj=None):
    #     return False
    #
    # # def has_add_permission(self, request):
    # #     return False
    #
    # def has_delete_permission(self, request, obj=None):
    #     return False


admin.site.register(Student, User)
