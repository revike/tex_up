from django.contrib import admin

from main_app.models import Client




class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'phone')
    list_display_links = ('first_name', 'phone')
    readonly_fields = ('first_name', 'phone',)


admin.site.register(Client, ClientAdmin)
admin.site.site_header = 'Админ-панель Tex_UP'