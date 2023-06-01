from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User, Employee


@admin.display(description='Full Name')
def full_name(obj):
    return "%s %s" % (obj.first_name, obj.last_name)


class CustomUser(UserAdmin):
    ordering = ('-date_joined',)
    list_display = (
        'username', 'email',
        full_name,
        'is_active',
    )

    list_filter = ('is_active', 'is_staff', 'is_superuser',)

    fieldsets = (
        (None, {
            # 'classes': ('collapse',),
            'fields': ('username', 'password')
        }),
        ('Personal Info', {
            'fields': (('first_name', 'last_name'),
                       'email', 'birth_date', 'photo',)
        }),
        ('Fundamental Permissions', {
            'classes': ('collapse',),
            'fields': ('is_active', 'is_staff', 'is_superuser',)
        }),
        ('Group Permissions', {
            'classes': ('collapse',),
            'fields': ('groups', 'user_permissions',)
        }),
        ('Important Dates', {
            'classes': ('collapse',),
            'fields': (('date_joined', 'last_modified'),)
        }),
    )


admin.site.register(User, CustomUser)
admin.site.register(Employee)
