from django.contrib import admin

from .models import FeeSubmissions


class FeeSubmissionsAdmin(admin.ModelAdmin):
    list_display = ('Semester', 'amount')

    def has_change_permission(self, request, obj=None):
        return False

    # def has_add_permission(self, request):
    #     return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(FeeSubmissions, FeeSubmissionsAdmin)
