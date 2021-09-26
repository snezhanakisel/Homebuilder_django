from django.contrib import admin
from .models import Carusel, Category, Mission, Contact


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


class ContactAdmin(admin.ModelAdmin):

    list_display = ('name', 'subject')


admin.site.register(Carusel)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Mission)
admin.site.register(Contact, ContactAdmin)
