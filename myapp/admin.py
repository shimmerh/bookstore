#coding:utf8
from django.contrib import admin

# Register your models here.


from models import Author, Publisher, Book


class PublisherAdmin(admin.ModelAdmin):
	"""
	If you are happy with the default admin
	interface,you don't need to define a 
	ModelAdmin object at all.you can register
	the model class without providing a ModelAdmin
	description
	"""
	# Set fieldsets to control the layout of adminn "add" and "change"
	# pages. The 'classes' ,  A list or tuple containing extra CSS
	# classes to apply to the fieldset.The 'description',which is
	# string of optional extra text to be displayed at the top of each
	# fieldset.
	fieldsets = (
		(None,{
			'fields': ('name',)
		}),
		(u'附加选项',{
			'classes': ('collapse', 'wide'),
			'fields': ('address', 'city', 'state_province', 'country', 'website'),
			'description': u'附加信息也是必填项',
		}),
	)

# The preceding example could be simplified to:
# If no instance name is provided(e.g Publisher)
# A default instance name of admin will be used
admin.site.register(Publisher,PublisherAdmin)

# There is also decorator for registering your ModelAdmin classes:
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	# Set list_display to control which fields are displayed on the
	# change list page of the admin
	list_display = ('name', 'title')
	
	#  
	date_hierarchy = 'birth_date'

	# The fields option to make simple layout changes in the forms on
	# the 'add' and 'change' pages
	fields = ('birth_date',)
	search_fields = ['name']
