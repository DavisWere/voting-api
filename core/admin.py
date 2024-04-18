from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.

from core.models import   User

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "Other Fields",
            {
                "fields": (
                   
                   
                )
            },
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Other Fields",
            {
                "fields": (
                    
                    "email",
                   

                )
            },
        ),
    )

admin.site.register(User, CustomUserAdmin)