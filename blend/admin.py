from django.contrib import admin
from .models import *
# Register your models here.

class DemoAdmin(admin.ModelAdmin):
    list_display=('email','created_on')

class ContactAdmin(admin.ModelAdmin):
    list_display=('email','message', 'created_on')  

class NewsletterAdmin(admin.ModelAdmin):
    list_display=('email','created_on')      

admin.site.register(Demo,DemoAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Newsletter,NewsletterAdmin)

