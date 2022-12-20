from django.contrib import admin

# Register your models here.
from crudApp.models import Details


class DetailsAdmin(admin.ModelAdmin):
    details=['name','age', 'address']


admin.site.register(Details,DetailsAdmin)
