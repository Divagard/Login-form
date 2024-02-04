from django.contrib import admin
from loginapp.models import logindb

# Register your models here.
class logindetails(admin.ModelAdmin):
    ls = ['username','password']
    
admin.site.register(logindb,logindetails)
