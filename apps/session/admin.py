from django.contrib import admin
from .models import Category, Car, Price, Percent


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ['narx']

    def narx(self, obj):
        return f"{obj.price // 1000},000 сўм соатига"


@admin.register(Percent)
class PercentAdmin(admin.ModelAdmin):
    list_display = ['foiz']

    def foiz(self, obj):
        return f"{obj.percent} %"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'toifa']


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'nomi']
