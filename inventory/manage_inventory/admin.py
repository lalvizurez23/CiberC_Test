from django.contrib import admin
from .models import inventory, upload_file

# Register your models here.
admin.site.register(inventory)
admin.site.register(upload_file)
