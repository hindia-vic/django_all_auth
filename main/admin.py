from django.contrib import admin
from  . models import Books,Review

class ReviewInline(admin.TabularInline):
  model = Review


class BooksAdmin(admin.ModelAdmin):
    inlines = [
ReviewInline,
]
    list_display = ("title", "author", "price")

admin.site.register(Books,BooksAdmin)

# Register your models here.
