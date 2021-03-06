from django.contrib import admin
from .models import*
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ['first_name', 'last_name', 'username', 'email', 'last_login', 'is_active', 'date_joined']
    list_display_links = ['email', 'first_name', 'last_name', 'username']
    readonly_fields = ['last_login', 'date_joined']
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()    

admin.site.register(Live)
admin.site.register(Prabhu)
admin.site.register(UpcomingEvent)
admin.site.register(TempleKirtan)
admin.site.register(FestivalTrack)
admin.site.register(Account, AccountAdmin)
admin.site.register(Playlist)
admin.site.register(Content)
admin.site.register(Audio)
admin.site.register(Notification)