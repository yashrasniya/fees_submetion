from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(branch)
class branch_admin(admin.ModelAdmin):
    pass


@admin.register(batch)
class batch_admin(admin.ModelAdmin):
    pass


@admin.register(semester)
class semester_admin(admin.ModelAdmin):
    pass
