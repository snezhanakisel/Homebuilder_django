from django.contrib import admin
from .models import Carusel, Category, Mission

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Carusel)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Mission)
