from django.db import models
from django.contrib import admin
class Book(models.Model):
    bookno=models.IntegerField(primary_key="bookno")
    bookname=models.CharField(max_length=20)
    authorname=models.CharField(max_length=40)
    publishdate=models.DateField()
    price=models.IntegerField()
class BookAdmin(admin.ModelAdmin):
    list_display=("bookno", "bookname", "authorname", "publishdate","price");
