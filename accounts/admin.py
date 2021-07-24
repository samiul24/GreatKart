from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

class AccountAdmin(UserAdmin):
    list_display=('email', 'username', 'first_name', 'last_name', 'join_date', 'is_active',)
    list_display_links=('email','username', 'first_name',)
    readonly_fields=('email', 'username', 'join_date',)
    ordering=('join_date',)

    filter_horizontal= ()
    list_filter=()
    fieldsets=()

admin.site.register(Account, AccountAdmin)