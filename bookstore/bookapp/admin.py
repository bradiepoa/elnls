from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Bookcategory)
class BookcategoryAdmin(admin.ModelAdmin):
	list_display = ('name','created_date','updated')

	list_filter = ('created_date','name' )
	search_fields = ('name','created_date')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('Title','Category','Author','isbn','Year_Published','Publisher','Uploaded_by')
	list_filter = ('Title','Category','Uploaded_by' )

admin.site.register(User)

admin.site.register(Chat)