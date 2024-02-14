from django.contrib import admin

# Register your models here.
from .models import EMmodel

class EMReorderFields(admin.ModelAdmin):
    fields = ['name','username','email','password','department','position','address']    # list of fields with the order of fields that are required to be displayed
    search_fields = ['username'] #use for search bar
    list_display = ('name','username','email','password','department','position','address','id') #use to show number not only object 1,obj2 etc
    list_filter = ('name', )
    
# registering the Question model
admin.site.register(EMmodel, EMReorderFields)