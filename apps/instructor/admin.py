from django.contrib import admin
from .models import Instructor, Tuman, TextInsUpdater, TextInsRegister


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ['id', 'ism', 'familiya', 'telefon', 'moshina']
    list_filter = ['toifa', 'tasdiqlash']
    exclude = ['ratet']


@admin.register(Tuman)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'nomi']


@admin.register(TextInsRegister)
class Name(admin.ModelAdmin):
    pass


@admin.register(TextInsUpdater)
class Name(admin.ModelAdmin):
    pass
