from django.contrib import admin

from users.models import User

# Register your models here.
admin.site.register(User)


class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'surname', 'email', 'phone')
    list_filter = ('first_name', 'surname',)
    search_fields = ('first_name', 'surname', 'email', 'phone',)
