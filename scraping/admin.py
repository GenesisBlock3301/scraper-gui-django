from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Trust)
admin.site.register(Facebook)
admin.site.register(GOOGLE)
admin.site.register(FeeFO)
admin.site.register(Youtube)