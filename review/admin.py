from django.contrib import admin

# Register your models here.
from .models import Review, Teacher, Contact

admin.site.register(Teacher)
admin.site.register(Review)
admin.site.register(Contact)
