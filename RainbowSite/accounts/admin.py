from django.contrib import admin
from .models import Lecturer,Secretary,User
# Register your models here.
admin.site.register(Lecturer)
admin.site.register(Secretary)
admin.site.register(User)