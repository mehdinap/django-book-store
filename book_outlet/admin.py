from django.contrib import admin

from .models import Book,Author,Address,Country
# Register your models here.

class BookAdmin(admin.ModelAdmin):
 #   readonly_fields=("slug",)   # this is alternative editable in model
    prepopulated_fields = {"slug":("title",)} # this is do when readonly_fields is not exist and do save method
    list_filter =("author","rating",)
    list_display=("title","author",)



admin.site.register(Book,BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)
