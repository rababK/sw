from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from data.models import VolunteerDay, gadeget ,report , advertisement , Comment
from .models import Users, supervisor
from .forms import UserCreationForm, UserChangeForm


class UsersAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'name', 'gender', 'type', 'is_staff',  'is_superuser')
    list_filter = ('is_superuser',)

    fieldsets = (
        (None, {'fields': ('email', 'is_staff', 'is_superuser', 'password')}),
        ('Personal info', {'fields': ('name', 'gender', 'type')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )

    add_fieldsets = (
         (None, {'fields': ('email', 'is_staff', 'is_superuser','password')}),
                ('Personal info', {'fields': ( 'name', 'gender', 'type')}),
                ('Groups', {'fields': ('groups',)}),
                ('Permissions', {'fields': ('user_permissions',)}),
    )

    search_fields = ('email', 'name')
    ordering = ('email',)
    filter_horizontal = ()



admin.site.register(Users, UsersAdmin)
admin.site.register(supervisor)
admin.site.register(VolunteerDay)
admin.site.register(advertisement)
admin.site.register(Comment)
admin.site.register(report)
admin.site.register(gadeget)
