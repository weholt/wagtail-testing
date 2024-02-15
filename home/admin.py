from django.contrib import admin
from .models import NonPage1, NonPage2


@admin.register(NonPage1)
class NonPage1Admin(admin.ModelAdmin):
    pass


@admin.register(NonPage2)
class NonPage2Admin(admin.ModelAdmin):
    pass
