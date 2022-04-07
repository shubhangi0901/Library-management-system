from django.contrib import admin
from .models import Book
from .models import Contact
# Register your models here.
@admin.register(Book)
class Bookadmin(admin.ModelAdmin):
    list_display = ['name','isbn','author','category']


@admin.register(Contact)
class Contactadmin(admin.ModelAdmin):
    list_display = ['name','email','feedback']


# Register your models here.
